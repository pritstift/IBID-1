from django import template 
from guardian.shortcuts import get_perms
from django.contrib.auth.models import Group
from ManageIdea.models import Idea
from ManageUsers.models import UserProfile
from ManageConnections.models import Membership
from ManageProjects.models import Note
from datetime import timedelta as td
register = template.Library()

@register.filter(name='can_view')
def can_view(user, instance): 
	return True if "view" in get_perms(user, instance) else False

@register.filter(name='can_edit')
def can_edit(user, instance):
	return True if "edit" in get_perms(user, instance) else False

@register.filter(name='has_group') 
def has_group(user, group_name): 
	group = Group.objects.get(name=group_name) 
	return True if group in user.groups.all() else False 

@register.filter(name='get_task')
def get_task(user, idea):
	return user.ideamembership_set.get(idea=idea).task

@register.filter(name='get_all_ideas')
def get_all_ideas(user):
	ideas=[]
	for membership in Membership.objects.filter(member=user, project=None):
		ideas.append(membership.idea)
	return  ideas

@register.filter(name='get_all_projects')
def get_all_ideas(user):
	projects=[]
	for membership in Membership.objects.filter(member=user, idea=None):
		projects.append(membership.project)
	return  projects

@register.filter(name='format_duration')
def format_duration(duration):
	t=dict()
	t["hours"], rem = divmod(duration.seconds,3600)
	t["minutes"], rem = divmod(rem,60)
	return str(t["hours"]) + 'h und ' + str(t["minutes"]) +'m'
@register.filter(name='total_duration')
def total_duration(notes):
	total=td(seconds=0)
	for note in notes:
		total=total+note.time_spend
	t=dict()
	t["hours"], rem = divmod(total.seconds,3600)
	t["minutes"], rem = divmod(rem,60)
	return str(t["hours"]) + 'h und ' + str(t["minutes"]) +'m'
	