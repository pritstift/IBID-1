from ManageUsers.models import UserProfile, UserProfilePrivacy
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions, InlineField, PrependedText


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


class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput(),help_text="Enter the same password as above, for verification.")
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	email = forms.EmailField(required=True)
	error_messages = {
		'password_mismatch': "The two password fields didn't match.",
	}
	class Meta:
		model = User
		fields = ('username','first_name','last_name',)
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['first_name'].label = "First name"
		self.fields['last_name'].label = "Last name"
		self.fields['username'].label = "Username"
		self.fields['email'].label = "Email"
		self.fields['password1'].label = "Password"
		self.fields['password2'].label = "Repeat Password"
		self.helper.layout=Layout(
			Div(
				'first_name',
				'last_name',
				'username',				
				'email',
				'password1',
				'password2',
				),
			FormActions(
				Submit('save', 'Submit'),
			),
		)
		
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and UserProfile.objects.filter(email_adress=email).count():
			raise forms.ValidationError('Email already exists')
		return email

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user

class UserEditForm(forms.ModelForm):
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('first_name','last_name')
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['first_name'].label = "First name"
		self.fields['last_name'].label = "Last name"
		self.helper.layout=Layout(
				Div(
					'first_name',
					'last_name',
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
		self.fields['email_adress'].label = "Email"
		self.fields['website'].label = "Web"
		self.fields['phone_number'].label = "Phone"
		self.fields['street'].label = "Street name"
		self.fields['house_number'].label = "House number"
		self.fields['zip_code'].label = "ZIP"
		self.fields['city'].label = "City"
		self.fields['company'].label = "Company"
		self.fields['user_type'].label = "User type"
		self.helper.layout=Layout(
			Div(
				'email_adress',
				'user_type',
				PrependedText('website','http://', placeholder='www.foo.org',active=True), 
				'phone_number',
				'street',
				'house_number',
				'zip_code',
				'city',
				'company',
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
		self.fields['website_ip'].label = "Website"
		self.fields['email_adress_ip'].label = "Email"
		self.fields['street_ip'].label = "Street name"
		self.fields['house_number_ip'].label = "House number"
		self.fields['zip_code_ip'].label = "ZIP"
		self.fields['city_ip'].label = "City"
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(
				'What information should be public to other users? </br>'
				),
			Div(
				'email_adress_ip',
				'phone_number_ip',
				'company_ip',
				'occupation_ip',
				'website_ip',
				'street_ip',
				'house_number_ip',
				'zip_code_ip',
				'city_ip',
				),
		)
		self.helper.form_tag = False

class SubmitForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(SubmitForm,self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			FormActions(
				Submit('submit', 'Save changes'),
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
			self.fields['website'].widget.attrs['disabled'] = True
			self.fields['email_adress'].widget.attrs['disabled'] = True
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'email_adress',
				'phone_number',
				'company',
				'website',
				css_class="tab-pane",
				css_id="profile",
				role="tabpanel" ,
				),
		)
