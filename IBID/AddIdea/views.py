from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from AddIdea.models import Idea

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

def post(request):
	if request.method == 'GET':
		return render(request, 'AddIdea/upload.html', {})
	elif request.method == 'POST':
		post = Idea.objects.create(title=request.POST['content'])
	return HttpResponseRedirect(reverse('AddIdea:index'))
