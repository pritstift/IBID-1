from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from ManageIdea.models import Idea
from django.contrib.auth.decorators import login_required
from ManageIdea.forms import PostForm
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from guardian.shortcuts import assign_perm
import re

@login_required
def detail(request, Idea_id):

	idea = get_object_or_404(Idea, pk=Idea_id)	
	#get_ip_fields(idea)
	return render(request, 'ManageIdea/detail.html', {'Idea':idea})

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
		idea=post_form.save(commit=False)
		print(get_ip_fields(idea))
		return render(request, 'ManageIdea/upload.html', {'post_form':post_form, 'idea':idea})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)

		#validate
		if post_form.is_valid():
			idea=post_form.save(commit=False)

			# add user and save to database
			idea.owner=request.user
			idea.save()
			post_form.save_m2m()
			Idea_id=idea.id
			assign_perm('view_idea', idea.owner,'idea')
			
			return HttpResponseRedirect(reverse('ManageIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'ManageIdea/upload.html', {'post_form':post_form})

	
def get_ip_fields(Instance):
	exclude_list = []
	fields=Instance._meta.get_fields()
	print(fields)
	ip_pattern=re.compile(r'.*_ip$')
	for i in fields:
		m=ip_pattern.match(i.name)
		if m:
			exclude_list.append(re.sub('_ip$','',m.group(0)))
	return exclude_list