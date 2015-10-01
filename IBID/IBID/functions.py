import re
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm, get_perms

from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

def get_ip_fields(Model):
	fieldList=[]
	ipList=[]
	fields=Model._meta.get_fields()
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		if i.concrete:
			m=ip_pattern.match(i.name)
			if m:
				ip_field=m.group(0)
				ipList.append(ip_field)
	return ipList

def get_ip_instance(PrivacyInstance,InstanceModel):
	ipList = []
	print ('in function:')
	modInstance = Object()
	fields=PrivacyInstance._meta.get_fields()
	modInstance.instance = InstanceModel()
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		if i.concrete:
			print(i.name)
			m=ip_pattern.match(i.name)
			if getattr(PrivacyInstance,i.name)==False:
				name=re.sub(r'_ip$','',m.group(0))
				ipList.append(name)
	print(ipList)
	for i in PrivacyInstance.instance._meta.get_fields():
		if i.concrete:
			if i.name not in ipList:
				print(getattr(PrivacyInstance.instance,i.name))
				setattr(modInstance.instance,i.name,getattr(PrivacyInstance.instance, i.name))
	return modInstance.instance




class Object(object):
	pass

def assign_permissions(**kwargs):
	staff = Group.objects.get(name='staff')
	assign_perm('view', kwargs["user"],kwargs["instance"])
	assign_perm('view', staff,kwargs["instance"])
	assign_perm('edit', staff,kwargs["instance"])
	assign_perm('edit', kwargs["user"],kwargs["instance"])

