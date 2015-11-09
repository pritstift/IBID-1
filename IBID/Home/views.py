from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User

from ManageIdea.models import Idea
from ManageUsers.models import UserProfile

 
def index(request):
	ideas=Idea.objects.all().order_by('-id')[:10]
	profiles=UserProfile.objects.all().order_by('-id')[:10]
	return render(request, 'Home/index.html',{'ideas':ideas,'profiles':profiles})
