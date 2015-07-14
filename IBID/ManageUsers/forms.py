from ManageUsers.models import UserProfile, UserProfilePrivacy
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name', 'password')
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'username',
				'email',
				'password',
				css_class="tab-pane active",
				css_id="user",
				role="tabpanel" ,
				),
			Div(
				'first_name',
				'last_name',
				css_class="tab-pane",
				css_id="personal_data",
				role="tabpanel" ,
				),
		)
		self.helper.form_tag = False

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude=['user','date_added','date_joined']
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'company',
				'occupation',
				'website',
				'website',
				css_class="tab-pane active",
				css_id="additional_data",
				role="tabpanel" ,
				),
			Div(
				'picture',
				'files',
				css_class="tab-pane",
				css_id="files",
				role="tabpanel" ,
				),
		)
		self.helper.form_tag = False

class PrivacyForm(forms.ModelForm):
	class Meta:
		model = UserProfilePrivacy
		exclude = ['instance']
	def __init__(self, *args, **kwargs):
		super(PrivacyForm,self).__init__(*args, **kwargs)
		self.fields['company_ip'].label = "Company"
		self.fields['occupation_ip'].label = "Occupation"
		self.fields['website_ip'].label = "Website"
		self.fields['picture_ip'].label = "Pictures"
		self.fields['files_ip'].label = "Files"
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'company_ip',
			    'occupation_ip',
			    'website_ip',
			    'picture_ip',
			    'files_ip',
				),
			FormActions(
				Submit('save', 'Save changes'),
				Button('cancel', 'Cancel'),
			),
		)
		self.helper[0].wrap(Div,css_id="privacy",role="tabpanel" , css_class="tab-pane")
		self.helper[1].wrap(Div,css_id="submit",role="tabpanel" , css_class="tab-pane")
		self.helper.form_tag = False

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
