import re
from django.contrib.auth.models import Group
from guardian.shortcuts import assign_perm, get_perms

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
	modInstance = Object()
	fields=PrivacyInstance._meta.get_fields()
	modInstance.instance = InstanceModel()
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		if i.concrete:
			m=ip_pattern.match(i.name)
			if getattr(PrivacyInstance,i.name)==True:
				name=re.sub(r'_ip$','',m.group(0))
				ipList.append(name)
	print(ipList)
	for i in PrivacyInstance.instance._meta.get_fields():
		if i.concrete:
			if i.name in ipList:
				setattr(modInstance.instance,i.name,getattr(PrivacyInstance.instance, i.name))
				print(i.name)
	return modInstance.instance




class Object(object):
	pass

def assign_permissions(**kwargs):
	staff = Group.objects.get(name='staff')
	assign_perm('view', kwargs["user"],kwargs["instance"])
	assign_perm('view', staff,kwargs["instance"])
	assign_perm('edit', staff,kwargs["instance"])
	assign_perm('edit', kwargs["user"],kwargs["instance"])