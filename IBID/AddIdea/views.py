from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from AddIdea.models import Idea
from django.contrib.auth.decorators import login_required
from AddIdea.forms import PostForm
from django.contrib.auth.models import User

@login_required
def detail(request, Idea_id):
	idea = get_object_or_404(Idea, pk=Idea_id)
	return render(request, 'AddIdea/detail.html', {'Idea':idea})

def index(request):
    latest_ideas = Idea.objects.order_by('-date_added')[:5]
    template = loader.get_template('AddIdea/index.html')
    context = RequestContext(request, {
        'latest_ideas': latest_ideas,
    })
    return HttpResponse(template.render(context))

@login_required
def post(request):
	if request.method == 'GET':
		post_form = PostForm()
		return render(request, 'AddIdea/upload.html', {'post_form':post_form})
	elif request.method == 'POST':
		#get PostForm data
		post_form=PostForm(data=request.POST)

		#validate
		if post_form.is_valid():
			idea=post_form.save(commit=False)

			# add user and save to database
			idea.owner=request.user
			idea.save()
			Idea_id=idea.id
			
			return HttpResponseRedirect(reverse('AddIdea:detail',args=[idea.id,]))
		#if form data is invalid
		else:
			print(post_form.errors)
			return render(request, 'AddIdea/upload.html', {'post_form':post_form})
	
