from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from ManageConnections.forms import AnnouncementForm, AddMemberForm, EditMemberForm
from ManageConnections.models import Announcement, Membership
from ManageIdea.models import Idea
from ManageProjects.models import Project
from ManageUsers.models import UserProfile
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, get_perms, remove_perm
from IBID.functions import get_ip_instance, assign_permissions, group_required, assign_staff_permissions

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


@login_required
def addmember(request, **kwargs):
	if "Idea_id" in kwargs:
		Idea_id = kwargs["Idea_id"]
		idea = get_object_or_404(Idea,pk=Idea_id)
		idea_flag = True
	elif "Project_id" in kwargs:
		Project_id = kwargs["Project_id"]
		project = get_object_or_404(Project,pk=Project_id)
		idea_flag = False
	if request.method=='POST':
		add_member_form = AddMemberForm(data=request.POST)
		if add_member_form.is_valid():
			membership = add_member_form.save(commit=False)
			if idea_flag:
				membership.idea = idea
			else :
				membership.project = project
			membership.save()
			assign_staff_permissions(instance=membership)
			can_edit=membership.can_edit
			if can_edit:
				if idea_flag :
					assign_permissions(user=membership.member, instance = idea)
				else:
					assign_permissions(user=membership.member, instance = project)
			else:
				if idea_flag:
					assign_perm('view', membership.member, idea)  
				else:
					assign_perm('view', membership.member, project)  
			if idea_flag:
				assign_permissions(user=idea.originator, instance=membership) 
				return HttpResponseRedirect(reverse('ManageIdea:detail', args=[Idea_id,]))
			else:
				return HttpResponseRedirect(reverse('ManageProjects:detail', args=[Project_id,]))
		else:
			if idea_flag:
				return render(request, 'ManageConnections/add_member.html',{'Idea':idea, 'add_member_form':add_member_form} )
			else:
				return render(request, 'ManageConnections/add_member.html',{'Project':project, 'add_member_form':add_member_form} )
	else:
		if idea_flag:
			if not 'edit' in get_perms(request.user, idea):
				return HttpResponse('No!')
			add_member_form = AddMemberForm(initial={'idea':idea.pk})
			return render(request, 'ManageConnections/add_member.html',{'Idea':idea, 'add_member_form':add_member_form} )
		else:
			if not 'edit' in get_perms(request.user, project):
				return HttpResponse('No!')
			add_member_form = AddMemberForm(initial={'project':project.pk})
			return render(request, 'ManageConnections/add_member.html',{'Project':project, 'add_member_form':add_member_form} )

@login_required
def edit_membership(request, **kwargs):
	Membership_id = kwargs.pop('Membership_id')
	membership=get_object_or_404(Membership,pk=Membership_id)
	if "Idea_id" in kwargs:
		Idea_id = kwargs["Idea_id"]
		idea = get_object_or_404(Idea,pk=Idea_id)
		idea_flag = True
	elif "Project_id" in kwargs:
		Project_id = kwargs["Project_id"]
		project = get_object_or_404(Project,pk=Project_id)
		idea_flag = False
	if request.method == 'GET':
		if not 'edit' in get_perms(request.user, membership):
			return HttpResponse('No!')
		edit_member_form = EditMemberForm(instance=membership)
		return render(request, 'ManageConnections/edit_member.html',{'Membership':membership,'edit_member_form':edit_member_form, 'idea_flag':idea_flag})
	elif request.method == 'POST':
		edit_member_form = EditMemberForm(data=request.POST, instance=membership)
		if edit_member_form.is_valid():
			membership=edit_member_form.save()
			if 'can_edit' in edit_member_form.changed_data:
				can_edit=edit_member_form.cleaned_data.get('can_edit')
				if can_edit:
					if idea_flag :
						assign_permissions(user=membership.member, instance = idea)
					else:
						assign_permissions(user=membership.member, instance = project)
				else:
					if idea_flag:
						remove_perm('edit', membership.member, idea) 
					else:
						remove_perm('edit', membership.member, project)
			if idea_flag:
				return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))
			else:
				return HttpResponseRedirect(reverse('ManageProjects:detail', args=[project.id,]))
		else:
			return render(request, 'ManageConnections/edit_member.html',{'edit_member_form':edit_member_form,'Membership':membership, 'idea_flag':idea_flag} )

@login_required
def remove_membership(Request_id,**kwargs):
	Membership_id=kwargs["Membership_id"]
	memberhsip=get_object_or_404(Membership, pk=Membership_id)
	memberhsip.delete()
	if "Idea_id" in kwargs:
		return HttpResponseRedirect(reverse('ManageIdea:detail', args=[kwargs["Idea_id"],]))
	elif "Project_id" in kwargs:
		return HttpResponseRedirect(reverse('ManageProjects:detail', args=[kwargs["Project_id"],]))
	