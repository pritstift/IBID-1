from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect 
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth  import authenticate


def userprofile(request,User_username):
	return render(request, 'ManageUsers/profile.html', {'User':User_username})

def auth(request):
	if request.method == 'GET':
		return render(request, 'ManageUsers/login.html', {})
	elif request.method == 'POST':
		uname=request.POST.get('Uname',None)
		passwd=request.POST.get('Passwd',None)
		user=authenticate(username=uname,password=passwd)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'User valid, active and authenticated')
			else:
				return render(request, 'Passwd valid, User inactive')
		else:
			render(request, 'Uname and Passwd incorrect')

def logout_user(request):
	logout(request)
	return render(request, 'ManageUsers/logout.html')
