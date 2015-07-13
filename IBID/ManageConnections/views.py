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
from guardian.shortcuts import assign_perm, get_perms

def index(request):
	announcements = Announcement.objects.all()
	template = loader.get_template('ManageConnections/index.html')
	context = RequestContext(request, {
		'announcements': announcements,
	})
	return HttpResponse(template.render(context))

@login_required
def post_announcement(request,**kwargs):
	if request.method == 'GET':
		if "Idea_id" in kwargs:
			Idea_id = kwargs["Idea_id"]
			idea = get_object_or_404(Idea,pk=Idea_id)
			if not "edit" in get_perms(request.user,idea):
				return HttpResponse("You have no permission for this idea")
		else:
			User_id = kwargs["User_id"]
			user=get_object_or_404(User, pk=User_id)
			userprofile = get_object_or_404(UserProfile,user=user)
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
				Idea_id = kwargs["Idea_id"]
				idea = get_object_or_404(Idea,pk=Idea_id)
				announcement.idea=idea
			announcement.owner=request.user
			announcement.save()
			staff = Group.objects.get(name='staff')
			assign_perm('edit', announcement.owner,announcement)
			assign_perm('edit', staff,announcement)
			return HttpResponseRedirect(reverse('ManageConnections:detail_announcement',args=[announcement.id]))
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
def edit_announcement(request, Request_id):
	pass
