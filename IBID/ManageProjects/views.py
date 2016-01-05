from datetime import datetime
import re
import random
import string
import Home

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

from IBID.functions import get_ip_instance, Object, group_required

from ManageProjects.models import Project, ProjectGroup, ProjectIdeas
from ManageProjects.forms import ProjectForm

from ManageIdea.models import Idea
from ManageIdea.views import assign_permissions

from ManageConnections.models import Membership

from guardian.shortcuts import assign_perm, get_perms


@login_required
def create_project(request,User_id):
	user = get_object_or_404(User,pk = User_id)
	
	if request.method == 'POST':
		project_form = ProjectForm(data = request.POST)
		
		if project_form.is_valid():
			project = project_form.save()
			group = Membership(member = user, project = project)
			group.save()
			assign_permissions(user=user, instance=project)
			assign_permissions(user=user, instance=group)
			return HttpResponseRedirect(reverse('ManageProjects:detail',args=[project.id,]))
		else:
			print(project_form.errors)

	else :
		project_form = ProjectForm()

	return render(request, 'ManageProjects/create_project.html',{'project_form':project_form})
		


@login_required
def detail(request, Project_id):
	project = get_object_or_404(Project, pk=Project_id)
	ideas = project.ideas.all()
	return render(request, 'ManageProjects/detail.html',{'project':project,'ideas':ideas})

@login_required
def edit_project(request,Project_id):
	pass

@login_required
def add_member(request, Project_id):
	pass

@group_required('admin', 'staff')
def add_measure(request, Project_id):
	project=get_object_or_404(Project, pk=Project_id)
	if request.method=='POST':
		projectmeasure_form=AddProjectMeasureForm(data=request.POST)
		if projectmeasure_form.is_valid():
			projectmeasure=projectmeasure_form.save(commit=False)
			projectmeasure.project=project
			projectmeasure.save()
			return HttpResponseRedirect(reverse('ManageProjects:detail', args=[project.id,]))
	elif request.method=='GET':
		projectmeasure_form=AddProjectMeasureForm()
	return render(request, 'ManageProjects/add_measure.html', {'Project':project, 'ProjectMeasureForm':projectmeasure_form})

# @group_required('admin', 'staff')
# def edit_measure(request,Measure_id):
# 	ideameasure=get_object_or_404(IdeaMeasures, pk=Measure_id)
# 	if request.method=='POST':
# 		ideameasure_form=AddIdeaMeasureForm(data=request.POST, instance=ideameasure)
# 		if ideameasure_form.is_valid():
# 			ideameasure=ideameasure_form.save()
# 			ideameasure.save()
# 			return HttpResponseRedirect(reverse('ManageIdea:detail', args=[ideameasure.idea.id,]))

# 	elif request.method=='GET':
# 		ideameasure_form=AddIdeaMeasureForm(instance=ideameasure)
# 	return render(request, 'ManageIdea/edit_measure.html', {'Measure':ideameasure,'IdeaMeasureForm':ideameasure_form})

# @group_required('admin', 'staff')
# def remove_measure(request, Measure_id):
# 	ideameasure=get_object_or_404(IdeaMeasures, pk=Measure_id)
# 	idea=ideameasure.idea
# 	ideameasure.delete()
# 	return HttpResponseRedirect(reverse('ManageIdea:detail', args=[idea.id,]))