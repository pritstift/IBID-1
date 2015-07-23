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
	class Meta:
		model = User
		fields = ('username','first_name','last_name', 'password')
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'first_name',
				'last_name',
				'username',				
				'password',
				css_class="tab-pane active",
				css_id="user_data",
				role="tabpanel" ,
				),
		)
		self.helper.form_tag = False

class UserEditForm(forms.ModelForm):
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('first_name','last_name')
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'first_name',
				'last_name',
				css_class="tab-pane active",
				css_id="user_data",
				role="tabpanel" ,
				),
		)
		self.helper.form_tag = False

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude=['user','date_joined']
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'phone_number',
				'company',
				'occupation',
				'website',
				'email_adress',
				css_class="tab-pane",
				css_id="additional_data",
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
		self.fields['phone_number_ip'].label = "Phone Number"
		self.fields['company_ip'].label = "Company"
		self.fields['occupation_ip'].label = "Occupation"
		self.fields['website_ip'].label = "Website"
		self.fields['email_adress_ip'].label = "Email"
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'email_adress_ip',
				'phone_number_ip',
				'company_ip',
				'occupation_ip',
				'website_ip',
				),
		)
		self.helper[0].wrap(Div,css_id="privacy",role="tabpanel" , css_class="tab-pane")
		self.helper[1].wrap(Div,css_id="submit",role="tabpanel" , css_class="tab-pane")
		self.helper.form_tag = False

class SubmitForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(SubmitForm,self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			FormActions(
				Submit('save', 'Save changes'),
				Button('cancel', 'Cancel'),
			),
		)
		self.helper.form_tag = False

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


class DisplayUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email','first_name','last_name')
	def __init__(self, *args, **kwargs):
		super(DisplayUserForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['username'].widget.attrs['disabled'] = True
			self.fields['email'].widget.attrs['disabled'] = True
			self.fields['first_name'].widget.attrs['disabled'] = True
			self.fields['last_name'].widget.attrs['disabled'] = True
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'username',
				'email',
				'first_name',
				'last_name',
				css_class="tab-pane active",
				css_id="user",
				role="tabpanel" ,
				),
		)

class DisplayProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user', 'date_joined']
	def __init__(self, *args, **kwargs):
		super(DisplayProfileForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['phone_number'].widget.attrs['disabled'] = True
			self.fields['company'].widget.attrs['disabled'] = True
			self.fields['occupation'].widget.attrs['disabled'] = True
			self.fields['website'].widget.attrs['disabled'] = True
			self.fields['email_adress'].widget.attrs['disabled'] = True
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'email_adress',
				'phone_number',
				'company',
				'occupation',
				'website',
				css_class="tab-pane",
				css_id="profile",
				role="tabpanel" ,
				),
		)
