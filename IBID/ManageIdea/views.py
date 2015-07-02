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
from ManageIdea.models import Idea, StatusRelationship, Status
from ManageIdea.forms import PostForm, StatusForm

@login_required
def detail(request, Idea_id):
	#check for 'view_idea' permission of authenticated user on certain idea
	idea = get_object_or_404(Idea, pk=Idea_id)
	if 'view_idea' in get_perms(request.user, idea):
		#has 'view_idea' permission
		print("user has permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':idea})
	else:
		#only print public fields
		print("user has no permission")
		return render(request, 'ManageIdea/detail.html', {'Idea':get_ip_instance(idea)})



def index(request):
    latest_ideas = Idea.objects.order_by('-date_added')[:5]
    template = loader.get_template('ManageIdea/index.html')
    context = RequestContext(request, {
        'latest_ideas': latest_ideas,
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
		return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'status_form':status_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)
		status_form = StatusForm(data=request.POST)
		print(request.POST)
		#validate
		if post_form.is_valid() and status_form.is_valid():
			idea=post_form.save(commit=False)
			# add user and save to database
			idea.owner=request.user
			idea.save()
			for state in status_form.status:
				statusRelationship = StatusRelationship.objects.create(idea = idea,status = state, species=request.POST.getlist('species')[state.id - 1])
			Idea_id=idea.id
			ideagroup = Group.objects.create(name=str(idea.title))
			assign_permissions(user=idea.owner,instance=idea)
			assign_perm('view_idea', ideagroup,idea)
			assign_perm('delete_idea', ideagroup,idea)
			assign_perm('change_idea', ideagroup,idea)
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form,'status_form':status_form})


def get_ip_instance(Instance):

	fieldList=[]
	ipList=[]
	modInstance = Object()
	fields=Instance._meta.get_fields()
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		if i.concrete:
			m=ip_pattern.match(i.name)
			i.name
			if m:
				ip_field=re.sub('_ip$','',m.group(0))
				print(ip_field)
				if getattr(Instance,ip_field+'_ip')==False:
					ipList.append(ip_field)
	for i in fields:
		if i.concrete:
			if i.name in ipList:
				pass
			else:
				fieldList.append(i.name)
	print(fieldList)
	for field in fieldList:
		setattr(modInstance,field,getattr(Instance, field))
	return modInstance


class Object(object):
	pass

def assign_permissions(**kwargs):
	staff = Group.objects.get(name='staff')
	assign_perm('view_idea', kwargs["user"],kwargs["instance"])
	assign_perm('delete_idea', kwargs["user"],kwargs["instance"])
	assign_perm('change_idea', kwargs["user"],kwargs["instance"])
	assign_perm('view_idea', staff,kwargs["instance"])
	assign_perm('delete_idea', staff,kwargs["instance"])
	assign_perm('change_idea', staff,kwargs["instance"])
