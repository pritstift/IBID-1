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

from guardian.shortcuts import assign_perm, get_perms


@login_required
def create_project(request,User_id):
	user = get_object_or_404(User,pk = User_id)
	
	if request.method == 'POST':
		project_form = ProjectForm(data = request.POST)
		
		if project_form.is_valid():
			project = project_form.save()
			group = ProjectGroup(user = user, project = project)
			group.save()
			assign_permissions(user=user, instance=project)
			return HttpResponseRedirect(reverse('ManageProjects:detail',args=[project.id,]))
		else:
			print(project_form.errors)

	else :
		project_form = ProjectForm()

	return render(request, 'ManageProjects/create_project.html',{'project_form':project_form})
		


@login_required
def detail(request, Project_id):
	project = get_object_or_404(Project, pk=Project_id)
	members = project.members.all()
	ideas = project.ideas.all()
	return render(request, 'ManageProjects/detail.html',{'project':project,'ideas':ideas,'members':members})

@login_required
def edit_project(request,Project_id):
	pass
	