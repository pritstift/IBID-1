from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from ManageConnections.forms import AnnouncementForm
from ManageConnections.models import Announcement
from ManageIdea.models import Idea
from ManageUsers.models import UserProfile
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, get_perms, remove_perm

def index(request):
	announcements = Announcement.objects.all()
	template = loader.get_template('ManageConnections/index.html')
	context = RequestContext(request, {
		'announcements': announcements,
	})
	return HttpResponse(template.render(context))

@login_required
def post_announcement(request,**kwargs):
	if "Idea_id" in kwargs:
		Idea_id = kwargs["Idea_id"]
		idea = get_object_or_404(Idea,pk=Idea_id)
	else:
		User_id = kwargs["User_id"]
		user=get_object_or_404(User, pk=User_id)
		userprofile = get_object_or_404(UserProfile,user=user)
	if request.method == 'GET':
		if "Idea_id" in kwargs:
			if not "edit" in get_perms(request.user,idea):
				return HttpResponse("You have no permission for this idea")
		elif "User_id" in kwargs:
			if not "edit" in get_perms(request.user,userprofile):
				return HttpResponse(" You have no permission for this Userprofile")
		post_form = AnnouncementForm()
		return render(request, 'ManageConnections/post_announcement.html', {'post_form':post_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=AnnouncementForm(data=request.POST)
		#validate
		if post_form.is_valid():
			announcement=post_form.save(commit=False)
			# add user and save to database
			if "Idea_id" in kwargs:
				announcement.idea=idea
				announcement.owner=idea.owner
			else:
				announcement.owner = user
			announcement.save()
			staff = Group.objects.get(name='staff')
			assign_perm('edit', announcement.owner,announcement)
			assign_perm('edit', staff,announcement)
			if "Idea_id" in kwargs:
				return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id]))
			elif "User_id" in kwargs:
				return HttpResponseRedirect(reverse('ManageUsers:userprofile',args=[user.id]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageConnections/post_announcement.html', {'post_form':post_form})

@login_required
def detail_announcement(request, Request_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	announcement = get_object_or_404(Announcement, pk=Request_id)
	return render(request, 'ManageConnections/detail_announcement.html', {'announcement':announcement})

@login_required
def edit_announcement(request, **kwargs):
	if "Idea_id" in kwargs:
		Idea_id = kwargs["Idea_id"]
		idea = get_object_or_404(Idea,pk=Idea_id)
	else:
		User_id = kwargs["User_id"]
		user=get_object_or_404(User, pk=User_id)
		userprofile = get_object_or_404(UserProfile,user=user)
	Request_id=kwargs["Request_id"]
	announcement=get_object_or_404(Announcement, pk=Request_id)
	if request.method=='POST':
		''' Check for edit permissions on announcement'''
		if not request.user.has_perm('edit', announcement):
			return HttpResponse('No!')
		announcement_form=AnnouncementForm(data=request.POST, instance=announcement)

		if announcement_form.is_valid():
			'''If Form is valid: save und return to the page of the idea'''
			announcement.save()
			if "Idea_id" in kwargs:
				return HttpResponseRedirect(reverse('ManageIdea:detail', args=[kwargs["Idea_id"],]))
			elif "User_id" in kwargs:
				return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[kwargs["User_id"],]))
	elif request.method=='GET':
		announcement_form=AnnouncementForm(instance=announcement)
		if "Idea_id" in kwargs:
			return render(request,'ManageConnections/edit_announcement.html',{'announcement':announcement,'announcement_form':announcement_form,'isidea':True})
		elif "User_id" in kwargs:
			return render(request,'ManageConnections/edit_announcement.html',{'announcement':announcement,'announcement_form':announcement_form,'isidea':False})

@login_required
def remove_announcement(request, **kwargs):
	Request_id=kwargs["Request_id"]
	announcement=get_object_or_404(Announcement, pk=Request_id)
	announcement.delete()
	if "Idea_id" in kwargs:
		return HttpResponseRedirect(reverse('ManageIdea:detail', args=[kwargs["Idea_id"],]))
	elif "User_id" in kwargs:
		return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[kwargs["User_id"],]))


