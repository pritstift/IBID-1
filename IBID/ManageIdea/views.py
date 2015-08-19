from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, get_perms
from django.forms.models import modelform_factory
import re
from ManageIdea.models import Idea, IdeaPrivacy
from ManageIdea.forms import PostForm, PrivacyForm, DisplayIdeaForm
from ManageConnections.models import Announcement

from IBID.functions import get_ip_instance, assign_permissions

@login_required
def detail(request, Idea_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea = get_object_or_404(Idea, pk=Idea_id)
	ideaprivacy = get_object_or_404(IdeaPrivacy, instance=idea)
	detail_form = DisplayIdeaForm(instance=idea)
	announcements = Announcement.objects.filter(idea=idea)
	perms = get_perms(request.user, idea)
	if 'edit' in perms:
		edit_idea = True
	else:
		edit_idea=False
	if ('view' or idea.title) in get_perms(request.user, idea):
		#has 'view_idea' permission
		print("user has permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':idea, 'detail_form':detail_form, 'announcements':announcements, 'edit_idea':edit_idea})
	else:
		#only print public fields
		print("user has no permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':get_ip_instance(ideaprivacy),'detail_form':detail_form, 'announcements':announcements, 'edit_idea':edit_idea})



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



