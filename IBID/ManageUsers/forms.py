from ManageUsers.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('occupation','website', 'picture')

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())
