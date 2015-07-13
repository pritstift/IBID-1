from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth  import authenticate, login
from ManageUsers.forms import UserForm, UserProfileForm, LoginForm, DisplayUserForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from ManageIdea.models import Idea
from ManageIdea.views import get_ip_instance, Object
from ManageUsers.models import UserProfile
from guardian.shortcuts import assign_perm, get_perms
from ManageIdea.views import assign_permissions
import Home
import re


@login_required
def userprofile(request,User_id):
	user = get_object_or_404(User,pk = User_id)
	userprofile = get_object_or_404(UserProfile,user=user)
	user_form = DisplayUserForm(instance = user)
	ideas=Idea.objects.filter(owner=user)
	if 'view' in get_perms(request.user,userprofile):
		return render(request, 'ManageUsers/profile.html', {'profile_form':userprofile,'user_form':user_form, 'ideas':ideas})
	else:
		return render(request, 'ManageUsers/profile.html', {'profile_form':get_ip_instance(userprofile),'user_form':user_form, 'ideas':ideas})


def logout_user(request):
	logout(request)
	return render(request, 'ManageUsers/logout.html')

def register(request):
	registered = False

	if request.method == 'POST':
		#grab information form from the POST data
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		#if the form is valid
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			#hash password and save
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user=user
			profile.save()
			assign_permissions(user=profile.user,instance=profile)

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			#save profile
			profile.save()

			#template registration was successful
			registered=True

			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			login(request, user)
		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print( user_form.errors, profile_form.errors)

	# GET
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	#render template
	return render(request, 'ManageUsers/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':

		#gather username and passwd from form
		login_form = LoginForm(data=request.POST)

		#validate
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']

			#authenticate
			user = authenticate(username=username, password=password)

			#if user is a User Object, there is a user and credentials where correct
			#else user == None
			if user:
				#active?
				if user.is_active:
					#log user in
					login(request,user)
					return HttpResponseRedirect(request.POST['next'])
				else:
					return HttpResponse("Your IBID account is inactive")
			else:
				print("Invalid login details: {0}, {1}".format(username, password))
				return HttpResponse("Invalid login details supplied.")

		else:
			print( login_form.errors)
			return render(request, 'ManageUsers/login.html', {'login_form':login_form})

	elif request.method == 'GET':
		#create empty forms to distribute
		login_form = LoginForm()

		if 'next' in request.GET:
			next=request.GET['next']
		else:
			next=reverse('Home:index')
			#render login template
		return render(request,'ManageUsers/login.html',{'login_form':login_form,'next':next})

@login_required
def edit(request, User_id):
	pass
