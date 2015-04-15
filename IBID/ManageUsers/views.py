from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth  import authenticate


def userprofile(request,User_username):
	return render(request, 'ManageUsers/profile.html', {'User':User_username})

def logout_user(request):
	logout(request)
	return render(request, 'ManageUsers/logout.html')
