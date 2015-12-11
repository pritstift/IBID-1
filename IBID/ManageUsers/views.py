from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth  import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import assign_perm, get_perms
from ManageUsers.forms import UserForm, UserProfileForm, LoginForm,  PrivacyForm, UserEditForm, SubmitForm, RegisterForm, UserPersonalityForm, CommentForm
from ManageUsers.models import UserProfile, UserProfilePrivacy, UserComment
from ManageIdea.models import Idea
from ManageIdea.views import assign_permissions
from ManageConnections.models import Announcement
from ManageProjects.models import Project, ProjectGroup
import Home
from IBID.functions import get_ip_instance, Object, group_required
import re
import random
import string


@login_required
def userprofile(request,User_id):
	user = get_object_or_404(User,pk = User_id)
	userprofile = get_object_or_404(UserProfile,user = user)
	projects = Project.objects.filter(projectgroup__user = user)
	announcements = Announcement.objects.filter(owner = user, idea=None)
	comments = UserComment.objects.filter(user = user)
	privacy = get_object_or_404(UserProfilePrivacy,instance = userprofile)
	ideas = Idea.objects.filter(originator = user)
	perms = get_perms(request.user,userprofile)
	if 'edit' in perms:
		edit_profile = user.id
	else:
		edit_profile=False
	if 'view' in perms:
		return render(request, 'ManageUsers/profile.html', {'ideas':ideas,'projects':projects,'announcements':announcements,'edit_profile':edit_profile, 'userprofile':userprofile, 'comments':comments})
	else:
		return render(request, 'ManageUsers/profile.html', {'ideas':ideas,'announcements':announcements, 'edit_profile':edit_profile,  'userprofile':get_ip_instance(privacy, UserProfile)})



def logout_user(request):
	logout(request)
	return render(request, 'ManageUsers/logout.html')

'''FOR INTERNAL USAGE: ONLY REGISTER USER IF REGISTERED'''
@login_required
def register(request):
	registered = False

	if request.method == 'POST':
		#grab information form from the POST data
		register_form = RegisterForm(data=request.POST)		
		#if the form is valid
		if register_form.is_valid():

			#hash password and save
			user=register_form.save(commit=False)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = UserProfile()
			profile.user=user
			profile.save()
			privacy = UserProfilePrivacy()
			privacy.instance = profile
			privacy.save()
			assign_permissions(user=profile.user,instance=profile)

			#template registration was successful
			registered=True


			#username = request.POST['username']
			#password = request.POST['password2']
			#user = authenticate(username=username, password=password)
			#login(request, user)
			return HttpResponseRedirect(reverse('ManageUsers:edit',args=[user.id,]))
		else:
			print( register_form.errors)
			return render(request, 'ManageUsers/register.html', {'register_form': register_form, 'registered': registered})
	# GET
	else:
		register_form = RegisterForm()
		#render template
		return render(request, 'ManageUsers/register.html', {'register_form': register_form })

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
	user = get_object_or_404(User,pk = User_id)
	profile = get_object_or_404(UserProfile, user=user)
	privacy=get_object_or_404(UserProfilePrivacy, instance=profile)
	if not 'edit' in get_perms(request.user, profile):
		return HttpResponse('You have no permissions to edit this profile')
	else:
		if request.method == 'POST':
			#grab information form from the POST data
			user_form=UserEditForm(data=request.POST, instance=user)
			profile_form = UserProfileForm(data=request.POST, instance=profile)
			privacy_form = PrivacyForm(data=request.POST, instance=privacy)
			personality_form=UserPersonalityForm(data=request.POST, instance=profile)
			#if the form is valid
			if  user_form.is_valid() and profile_form.is_valid() and privacy_form.is_valid() and personality_form.is_valid():
				user_form.save()
				profile.save()
				privacy.street_ip=privacy_form.cleaned_data['address_ip']
				privacy.house_number_ip=privacy_form.cleaned_data['address_ip']
				privacy.zip_code_ip=privacy_form.cleaned_data['address_ip']
				privacy.city_ip=privacy_form.cleaned_data['address_ip']
				privacy.save()
				return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[user.id,]))
			else:
				print('not valid')
				print( profile_form.errors, privacy_form.errors, personality_form.errors)

		# GET
		else:
			user_form=UserEditForm(instance=user)
			profile_form = UserProfileForm(instance=profile)
			personality_form = UserPersonalityForm(instance=profile)
			privacy_form = PrivacyForm(instance=privacy)
			#render template
			return render(request, 'ManageUsers/edit.html', {'user_form':user_form, 'profile_form': profile_form,'personality_form':personality_form,'privacy_form':privacy_form})

def sign_agreement(request, User_id):
	user = get_object_or_404(User,pk = User_id)
	profile = get_object_or_404(UserProfile, user=user)

@group_required('staff')
def createcomment(request, User_id):
	user=get_object_or_404(User,pk=User_id)
	if request.method =='POST':
		comment_form=CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment=comment_form.save(commit=False)
			comment.user=user
			comment.supervisor=request.user
			comment.save()
			staff = Group.objects.get(name='staff')
			assign_perm('view', staff,comment)
			assign_perm('edit', staff,comment)
		else:
			print(comment_form.errors)
		return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[User_id,]))
	
	elif request.method=='GET':
		comment_form=CommentForm()
		return render(request, 'ManageUsers/comment.html',{'comment_form':comment_form})

@group_required('staff')
def editcomment(request,Comment_id):
	comment=get_object_or_404(UserComment, pk=Comment_id)	
	if request.method=='POST':
		comment_form=CommentForm(data=request.POST, instance=comment)
		if comment_form.is_valid():
			comment=comment_form.save()
			comment.save()
		else:
			print(comment_form.errors)
		return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[comment.user.id,]))
	elif request.method=='GET':
		comment_form=CommentForm(instance=comment)
		return render(request, 'ManageUsers/edit_comment.html',{'comment_form':comment_form, 'Comment':comment})		

@group_required('staff')
def removecomment(request,Comment_id):
	comment=get_object_or_404(UserComment,pk=Comment_id)
	user=comment.user
	if not request.user.has_perm('edit',comment):
			return HttpResponse('No!')
	comment.delete()
	return HttpResponseRedirect(reverse('ManageUsers:userprofile', args=[user.id,]))
















