from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, get_perms, remove_perm
from django.forms.models import modelform_factory
from django.forms.formsets import formset_factory
import re
from ManageIdea.models import Idea, IdeaPrivacy, Comment, Measure, IdeaMeasures
from ManageIdea.forms import PostForm, PrivacyForm, DisplayIdeaForm, CommentForm, AddIdeaMeasureForm
from ManageConnections.models import Announcement, Membership

from IBID.functions import get_ip_instance, assign_permissions, group_required



@login_required
def detail(request, Idea_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea = get_object_or_404(Idea, pk=Idea_id)
	ideaprivacy = get_object_or_404(IdeaPrivacy, instance=idea)
	comments=Comment.objects.filter(idea=idea)
	commentform=CommentForm()
	detail_form = PostForm(instance=idea)
	print(detail_form.fields)
	for key in detail_form.fields:
		detail_form.fields[key].widget.attrs['readonly'] = True
	announcements = Announcement.objects.filter(idea=idea)
	perms = get_perms(request.user, idea)
	return render(request, 'ManageIdea/detail.html', {'Idea':idea,'IdeaPrivacy':ideaprivacy, 'detail_form':detail_form, 'announcements':announcements,'comments':comments, 'commentform':commentform})



@login_required
def removemember(request, Membership_id):
	membership=get_object_or_404(IdeaMembership,pk=Membership_id)
	idea=membership.idea
	if not 'edit' in get_perms(request.user, idea):
		return HttpResponse('No!')	
	membership.delete()
	return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))
	

@group_required('staff')
def createcomment(request, Idea_id):
	if request.method =='POST':
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment=comment_form.save(commit=False)
			comment.idea=Idea.objects.get(pk=Idea_id)
			comment.supervisor=request.user
			comment.save()
			if comment_form.cleaned_data['visible'] == True:
				assign_perm('view', comment.idea.owner,comment)
			staff = Group.objects.get(name='staff')
			assign_perm('view', staff,comment)
			assign_perm('edit', staff,comment)
		else:
			print(comment_form.errors)
		return HttpResponseRedirect(reverse('ManageIdea:detail', args=[Idea_id,]))


def editcomment(request, Comment_id):
	comment=get_object_or_404(Comment,pk=Comment_id)
	if request.method=='POST':
		comment_form=CommentForm(data=request.POST, instance=comment)
		if comment_form.is_valid():
			comment.save()
			if comment_form.cleaned_data['visible'] == True:
				assign_perm('view', comment.idea.owner,comment)
			else:
				remove_perm('view', comment.idea.owner,comment)
			staff = Group.objects.get(name='staff')
			assign_perm('view', staff,comment)
			assign_perm('edit', staff,comment)
			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[comment.idea.id,]))
	elif request.method=='GET':
		if not request.user.has_perm('edit',comment):
			return HttpResponse('No!')
		comment_form=CommentForm(instance=comment)
		comment_form.fields['visible'].initial=comment.idea.owner.has_perm('view',comment)
	return render(request, 'ManageIdea/edit_comment.html',{'Comment':comment,'comment_form':comment_form})


def removecomment(request, Comment_id):
	comment=get_object_or_404(Comment,pk=Comment_id)
	idea=comment.idea
	if not request.user.has_perm('edit',comment):
			return HttpResponse('No!')
	comment.delete()
	return HttpResponseRedirect(reverse('ManageIdea:detail', args=[comment.idea.id,]))

def index(request):
	all_ideas = Idea.objects.all()
	template = loader.get_template('ManageIdea/index.html')
	context = RequestContext(request, {
		'latest_ideas': all_ideas,
	})
	return HttpResponse(template.render(context))

@login_required
def edit(request, Idea_id):
	idea=get_object_or_404(Idea, pk=Idea_id)
	privacy=get_object_or_404(IdeaPrivacy, instance=idea)
	if request.method == 'GET':
		if not request.user.has_perm('edit', idea):
			return HttpResponse('No!')
		post_form = PostForm(instance=idea)
		privacy_form = PrivacyForm(instance=privacy)
		return render(request, 'ManageIdea/edit.html', {'post_form':post_form, 'privacy_form':privacy_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(request.POST,request.FILES, instance=idea)
		privacy_form = PrivacyForm(data=request.POST, instance=privacy)
		#print(request.POST)
		#validate
		if post_form.is_valid() and privacy_form.is_valid():			
			print(request.FILES)
			if 'pictures' in request.FILES:
				print('pictures')
				idea.pictures=request.FILES['pictures']
			# add user and save to database
			post_form.save()
			idea.save()
			privacy.save()
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/edit.html', {'post_form':post_form,'privacy_form':privacy_form})


@login_required
def post(request, User_id):
	user=get_object_or_404(User, pk=User_id)
	if request.method == 'GET':
		post_form = PostForm(initial={'originator':user})
		return render(request, 'ManageIdea/upload.html', {'post_form':post_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)
		privacy_form = PrivacyForm(data=request.POST)
		#print(request.POST)
		#validate
		if post_form.is_valid() and privacy_form.is_valid():
			idea=post_form.save(commit=False)
			# add user and save to database
			idea.originator=user
			idea.save()
			post_form.save_m2m()
			privacy=privacy_form.save(commit=False)
			privacy.instance = idea
			privacy.save()
			membership=Membership.objects.create(idea=idea, member=idea.originator, task="Ideengeber")
			assign_permissions(user=idea.originator, instance=idea)
			assign_permissions(user=idea.originator, instance=membership)
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'privacy_form':privacy_form})

@group_required('admin', 'staff')
def add_idea_measure(request, Idea_id):
	idea=get_object_or_404(Idea, pk=Idea_id)
	if request.method=='POST':
		ideameasure_form=AddIdeaMeasureForm(data=request.POST)
		if ideameasure_form.is_valid():
			ideameasure=ideameasure_form.save(commit=False)
			ideameasure.idea=idea
			ideameasure.save()
			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))
	elif request.method=='GET':
		ideameasure_form=AddIdeaMeasureForm()
	return render(request, 'ManageIdea/add_measure.html', {'Idea':idea, 'IdeaMeasureForm':ideameasure_form})

@group_required('admin', 'staff')
def edit_measure(request,Measure_id):
	ideameasure=get_object_or_404(IdeaMeasures, pk=Measure_id)
	if request.method=='POST':
		ideameasure_form=AddIdeaMeasureForm(data=request.POST, instance=ideameasure)
		if ideameasure_form.is_valid():
			ideameasure=ideameasure_form.save()
			ideameasure.save()
			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[ideameasure.idea.id,]))

	elif request.method=='GET':
		ideameasure_form=AddIdeaMeasureForm(instance=ideameasure)
	return render(request, 'ManageIdea/edit_measure.html', {'Measure':ideameasure,'IdeaMeasureForm':ideameasure_form})

@group_required('admin', 'staff')
def remove_measure(request, Measure_id):
	ideameasure=get_object_or_404(IdeaMeasures, pk=Measure_id)
	idea=ideameasure.idea
	ideameasure.delete()
	return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))