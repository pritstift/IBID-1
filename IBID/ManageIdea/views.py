from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from taggit.managers import TaggableManager
from guardian.shortcuts import assign_perm, get_perms
import re
from ManageIdea.models import Idea, StatusRelationship, Status, IdeaPrivacy
from ManageIdea.forms import PostForm, StatusForm, PrivacyForm

@login_required
def detail(request, Idea_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea = get_object_or_404(Idea, pk=Idea_id)
	if ('view' or idea.title) in get_perms(request.user, idea):
		#has 'view_idea' permission
		print("user has permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':idea})
	else:
		#only print public fields
		print("user has no permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':get_ip_instance(idea)})



def index(request):
	all_ideas = Idea.objects.all()
	template = loader.get_template('ManageIdea/index.html')
	context = RequestContext(request, {
		'latest_ideas': all_ideas,
	})
	return HttpResponse(template.render(context))

def edit(request, Idea_id):
	idea = get_object_or_404(Idea, pk=Idea_id)
	return render(request, 'ManageIdea/detail.html', {'Idea':idea})

@login_required
def post(request):
	if request.method == 'GET':
		post_form = PostForm()
		status_form = StatusForm()
		privacy_form = PrivacyForm()
		return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'status_form':status_form, 'privacy_form':privacy_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)
		status_form = StatusForm(data=request.POST)
		privacy_form = PrivacyForm(data=request.POST)
		#print(request.POST)
		#validate
		if post_form.is_valid() and status_form.is_valid() and privacy_form.is_valid():
			idea=post_form.save(commit=False)
			# add user and save to database
			idea.owner=request.user
			idea.save()
			privacy=privacy_form.save(commit=False)
			privacy.idea = idea
			privacy.save()
			for state in status_form.status:
				statusRelationship = StatusRelationship.objects.create(idea = idea,status = state, species=request.POST.getlist('species')[state.id - 1])
			Idea_id=idea.id
			post_form.save_m2m()
			ideagroup = Group.objects.create(name=idea.title)
			ideagroup.user_set.add(idea.owner)
			assign_permissions(user=idea.owner,instance=idea)
			assign_perm('view', ideagroup,idea)
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'status_form':status_form, 'privacy_form':privacy_form})


def get_ip_instance(Instance):
	ipList = []
	modInstance = Object()
	privacyInstance = IdeaPrivacy.objects.get(idea=Instance)
	fields=privacyInstance._meta.get_fields()
	modInstance.idea = Instance
	for i in fields:
		if i.concrete:
			if getattr(privacyInstance,i.name)==True:
				ipList.append(i.name)
	for i in Instance._meta.get_fields():
		if i.concrete:
			if i.name not in ipList:
				setattr(modInstance,i.name,getattr(Instance, i.name))
	return modInstance




class Object(object):
	pass

def assign_permissions(**kwargs):
	staff = Group.objects.get(name='staff')
	assign_perm('view', kwargs["user"],kwargs["instance"])
	assign_perm('view', staff,kwargs["instance"])
	assign_perm('edit', staff,kwargs["instance"])
	assign_perm('edit', kwargs["user"],kwargs["instance"])
