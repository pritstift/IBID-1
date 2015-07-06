from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from ManageConnections.forms import AnnounceIdeaForm, AnnounceUserForm
from ManageConnections.models import AnnounceIdea, AnnounceUser
from ManageIdea.models import Idea
from django.contrib.auth.models import User, Group
from ManageIdea.views import assign_permissions

@login_required
def post_idea_request(request, Idea_id):
	if request.method == 'GET':
		post_form = AnnounceIdeaForm()
		idea = get_object_or_404(Idea,pk=Idea_id)
		return render(request, 'ManageConnections/upload_idea_request.html', {'post_form':post_form})
	elif request.method == 'POST':
		#get PostForm data
		idea = get_object_or_404(Idea,pk=Idea_id)
		post_form=AnnounceIdeaForm(data=request.POST)
		#validate
		if post_form.is_valid():
			idea_request=post_form.save(commit=False)
			# add user and save to database
			idea_request.idea=idea
			idea_request.owner=request.user
			idea_request.save()
			assign_permissions(user=idea_request.owner,instance=idea_request)
			return HttpResponseRedirect(reverse('ManageConnections:detail_idea_request',args=[idea_request.id]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageConnections/upload_idea_request.html', {'post_form':post_form})

@login_required
def detail_idea_request(request, Request_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea_request = get_object_or_404(AnnounceIdea, pk=Request_id)
	return render(request, 'ManageConnections/detail_idea_request.html', {'Idea_request':idea_request})

@login_required
def post_user_request(request):
	if request.method == 'GET':
		post_form = AnnounceUserForm()
		return render(request, 'ManageConnections/upload_user_request.html', {'post_form':post_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=AnnounceUserForm(data=request.POST)
		#validate
		if post_form.is_valid():
			user_request=post_form.save(commit=False)
			# add user and save to database
			user_request.owner=request.user
			user_request.save()
			assign_permissions(user=user_request.owner,instance=user_request)
			return HttpResponseRedirect(reverse('ManageConnections:detail_user_request',args=[user_request.id]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageConnections/upload_user_request.html', {'post_form':post_form})

@login_required
def detail_user_request(request, Request_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	user_request = get_object_or_404(AnnounceUser, pk=Request_id)
	return render(request, 'ManageConnections/detail_user_request.html', {'User_request':user_request})
