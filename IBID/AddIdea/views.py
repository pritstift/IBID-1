from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from AddIdea import models as m
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
def post_detail(request, post_id):
    try:
        post = m.Post.objects.get(pk=post_id)
    except m.Post.DoesNotExist:
        # If no Post has id post_id, we raise an HTTP 404 error.
        raise HttpResponse("Http404")
    return render(request, 'detail.html', {'post': post})

def post_upload(request):
    if request.method == 'GET':
        return render(request, 'post/upload.html', {})
    elif request.method == 'POST':
        post = m.Post.objects.create(content=request.POST['content'],
                                     created_at=datetime.utcnow())
  
        return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))
