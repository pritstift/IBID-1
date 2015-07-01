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
		exclude=['user','date_added','date_joined']

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class DisplayUserForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name')
