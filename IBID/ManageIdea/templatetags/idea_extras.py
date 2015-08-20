from django import template 
from guardian.shortcuts import get_perms
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='can_view')
def can_view(user, instance): 
	return True if "view" in get_perms(user, instance) else False

@register.filter(name='has_group') 
def has_group(user, group_name): 
	group = Group.objects.get(name=group_name) 
	return True if group in user.groups.all() else False 