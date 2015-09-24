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
from ManageIdea.models import Idea, IdeaPrivacy, Comment, IdeaMembership
from ManageIdea.forms import PostForm, PrivacyForm, DisplayIdeaForm, CommentForm, AddMemberForm, EditMemberForm
from ManageConnections.models import Announcement

from IBID.functions import get_ip_instance, assign_permissions



@login_required
def detail(request, Idea_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea = get_object_or_404(Idea, pk=Idea_id)
	ideaprivacy = get_object_or_404(IdeaPrivacy, instance=idea)
	comments=Comment.objects.filter(idea=idea)
	commentform=CommentForm()
	detail_form = DisplayIdeaForm(instance=idea)
	announcements = Announcement.objects.filter(idea=idea)
	perms = get_perms(request.user, idea)
	return render(request, 'ManageIdea/detail.html', {'Idea':idea,'IdeaPrivacy':ideaprivacy, 'detail_form':detail_form, 'announcements':announcements,'comments':comments, 'commentform':commentform})

@login_required
def addmember(request, Idea_id):
	idea=get_object_or_404(Idea,pk=Idea_id)
	if request.method=='POST':
		add_member_form = AddMemberForm(data=request.POST)
		if add_member_form.is_valid():
			membership = add_member_form.save(commit=False)
			membership.idea=idea
			username=add_member_form.cleaned_data.get('username')
			membership.member=User.objects.get(username=username)
			membership.save()
			can_edit=add_member_form.cleaned_data.get('can_edit')
			if can_edit:
				assign_permissions(user=membership.member, instance = idea)
			else:
				assign_perm('view', membership.member, idea)

			assign_permissions(user=idea.owner,instance=membership)
			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[Idea_id,]))
		else:
			print(add_member_form.errors)
			return render(request, 'ManageIdea/add_member.html',{'Idea':idea, 'add_member_form':add_member_form} )
	else:
		if not 'edit' in get_perms(request.user, idea):
			return HttpResponse('No!')
		add_member_form = AddMemberForm()
	return render(request, 'ManageIdea/add_member.html',{'Idea':idea, 'add_member_form':add_member_form} )

@login_required
def editmember(request, Membership_id):
	membership=get_object_or_404(IdeaMembership,pk=Membership_id)
	idea=membership.idea
	if request.method == 'GET':
		if not 'edit' in get_perms(request.user, idea):
			return HttpResponse('No!')
		edit_member_form = EditMemberForm(instance=membership)
		edit_member_form.fields['can_edit'].initial=membership.member.has_perm('edit', idea)
		return render(request, 'ManageIdea/edit_member.html',{'Idea':idea,'Membership':membership,'edit_member_form':edit_member_form})
	elif request.method == 'POST':
		edit_member_form = EditMemberForm(data=request.POST)
		if edit_member_form.is_valid():
			print("is valid")
			membership.task=edit_member_form.cleaned_data['task'] 
			membership.save()
			can_edit=edit_member_form.cleaned_data.get('can_edit')
			if can_edit:
				assign_permissions(user=membership.member, instance = idea)
			else:
				remove_perm('edit', membership.member, idea)
				assign_perm('view', membership.member, idea)
			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))
		else:
			return render(request, 'ManageIdea/edit_member.html',{'Idea':idea, 'edit_member_form':edit_member_form} )
	
@login_required
def removemember(request, Membership_id):
	membership=get_object_or_404(IdeaMembership,pk=Membership_id)
	idea=membership.idea
	print("in delete member function")
	if not 'edit' in get_perms(request.user, idea):
		return HttpResponse('No!')	

	membership.delete()
	return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))
	

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
			print("form not valid")
			print(comment_form.errors)
		return HttpResponseRedirect(reverse('ManageIdea:detail', args=[Idea_id,]))

def index(request):
	all_ideas = Idea.objects.all()
	template = loader.get_template('ManageIdea/index.html')
	context = RequestContext(request, {
		'latest_ideas': all_ideas,
	})
	return HttpResponse(template.render(context))

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
		if post_form.is_valid()  and privacy_form.is_valid():			
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
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'privacy_form':privacy_form})


@login_required
def post(request):
	if request.method == 'GET':
		post_form = PostForm()
		privacy_form = PrivacyForm()
		return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'privacy_form':privacy_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)
		privacy_form = PrivacyForm(data=request.POST)
		#print(request.POST)
		#validate
		if post_form.is_valid() and privacy_form.is_valid():
			idea=post_form.save(commit=False)
			# add user and save to database
			idea.owner=request.user
			idea.save()
			Idea_id=idea.id
			post_form.save_m2m()
			privacy=privacy_form.save(commit=False)
			privacy.instance = idea
			privacy.save()
			ideagroup = Group.objects.create(name=idea.title)
			ideagroup.user_set.add(idea.owner)
			assign_permissions(user=idea.owner,instance=idea)
			assign_perm('view', ideagroup,idea)
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'privacy_form':privacy_form})



