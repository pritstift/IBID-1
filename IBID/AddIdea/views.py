from django.http import HttpResponse
from django.template import RequestContext, loader

from AddIdea.models import Idea

def detail(request, Idea_id):
    return HttpResponse("You're looking at idea %s." % Idea_id)

def index(request):
    latest_ideas = Idea.objects.order_by('-date_added')[:5]
    template = loader.get_template('AddIdea/index.html')
    context = RequestContext(request, {
        'latest_ideas': latest_ideas,
    })
    return HttpResponse(template.render(context))
