from ManageUsers.models import UserProfile, UserProfilePrivacy, UserComment
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
	''' FOR INTERNAL USE OUTCOMMENTED
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput(),help_text="Enter the same password as above, for verification.")
	error_messages = {
		'password_mismatch': "The two password fields didn't match.",
	}
	'''
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	username = forms.EmailField(required=True)	
	class Meta:
		model = User
		fields = ('first_name','last_name','username')
	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['first_name'].label = "Vorname"
		self.fields['last_name'].label = "Nachname"
		self.fields['username'].label = "Email"
		''' FOR INTERNAL USE OUTCOMMENTED
		self.fields['password1'].label = "Password"
		self.fields['password2'].label = "Repeat Password"
		self.fields['username'].label = "Username"
		'''
		self.helper.layout=Layout(
			Div(
				'first_name',
				'last_name',			
				'username',
				''' FOR INTERNAL USE OUTCOMMENTED
				'username',	
				'password1',
				'password2',
				'''
				),
			FormActions(
				Submit('save', 'Nutzer Anlegen'),
			),
		)
	''' FOR INTERNAL USE OUTCOMMENTED	
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2
	'''
	def clean_email(self):
		email = self.cleaned_data.get('email')
		if email and UserProfile.objects.filter(email_adress=email).count():
			raise forms.ValidationError('Diese Email existiert bereits')
		return email

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)

		'''FOR INTERNAL USE AUTOGENERATED PWD'''
		password = User.objects.make_random_password()
		user.set_password(password)
		if commit:
			user.save()
		return user
    

class UserEditForm(forms.ModelForm):
	first_name=forms.CharField(required=True)
	last_name=forms.CharField(required=True)
	username = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('first_name','last_name', 'username')
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['first_name'].label = "Vorname"
		self.fields['last_name'].label = "Nachnahme"
		self.fields['username'].label = "Email"
		self.helper.layout=Layout(
				Div(
					'first_name',
					'last_name',
					'username',
					),
		)
		self.helper.form_tag = False

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields=['street', 'house_number', 'zip_code', 'city', 'company', 'website','phone_number', 'user_type']
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['website'].label = "Web"
		self.fields['phone_number'].label = "Telefon"
		self.fields['street'].label = "Straße"
		self.fields['house_number'].label = "Hausnummer"
		self.fields['zip_code'].label = "PLZ"
		self.fields['city'].label = "Ort"
		self.fields['company'].label = "Firmenname"
		self.fields['user_type'].label = "Nutzertyp"
		self.helper.layout=Layout(
			Div(
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
	address_ip = forms.BooleanField(required=False, initial=False)
	class Meta:
		model = UserProfilePrivacy
		exclude = ['instance', 'street_ip', 'house_number_ip', 'zip_code_ip', 'city_ip']
	def __init__(self, *args, **kwargs):
		super(PrivacyForm,self).__init__(*args, **kwargs)
		self.fields['phone_number_ip'].label = "Phone Number"
		self.fields['company_ip'].label = "Company"
		self.fields['website_ip'].label = "Website"
		self.fields['address_ip'].label = "Address"
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML(
				'What information should be public to other users? </br>'
				),
			Div(
				'phone_number_ip',
				'company_ip',
				'website_ip',
				'address_ip',
				),
		)
		self.helper.form_tag = False

class UserPersonalityForm(forms.ModelForm):
	""" Form für die Erfassung der Gründereignung """
	class Meta:
		model=UserProfile
		fields =['education','skills']
	def __init__(self,*args,**kwargs):
		super(UserPersonalityForm,self).__init__(*args,**kwargs)
		self.fields['skills'].label = "Fähigkeiten"
		self.fields['education'].label = "Ausbildung"
		self.helper=FormHelper()
		self.helper.form_tag = False
		self.helper.layout=Layout(
			Div(
				'skills',
				'education',

			),
		)
		
class PersonalityForm(forms.ModelForm):
	""" Form für die Erfassung der Gründereignung """
	class Meta:
		model=UserProfile
		exclude =['education','sklills','user','date_joined', 'street', 'house_number', 'zip_code', 'city', 'company', 'website','phone_number', 'user_type']
	def __init__(self,*args,**kwargs):
		super(PersonalityForm,self).__init__(*args,**kwargs)
		self.fields['role'].label = "Rolle im Gründerteam"
		self.fields['seeks_opportunity'].label = "Nutzt Gelegenheit"
		self.fields['delayed_gratifikation'].label = "Delayed Gratification"
		self.fields['target_oriented'].label = "Zielorientiert"
		self.fields['flexible_thinker'].label = "Kann schnell umdenken"
		self.fields['social_stable'].label = "Soziale Stabilität"
		self.fields['curious'].label = "Neugierig"
		self.fields['responsible'].label = "Verantwortungsbewusst"
		self.fields['risk_taking'].label = "Nimmt risiken in Kauf"
		self.fields['determined'].label = "Selbstbestimmt"
		self.fields['stamina'].label = "Durchhaltevermögen"
		self.helper=FormHelper()
		self.helper.form_tag = False
		self.helper.layout=Layout(
			Div(
				'role',
				'seeks_opportunity',
				'delayed_gratifikation',
				'target_oriented',
				'flexible_thinker',
				'social_stable',
				'curious',
				'responsible',
				'risk_taking',
				'determined',
				'stamina',
			),
		)


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

class CommentForm(forms.ModelForm):
	title = forms.CharField( required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)
	class Meta:
		model = UserComment
		exclude = ['supervisor','user', 'date_added','idea']
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.fields['title'].label = "Title"
		self.fields['message'].label = "Message"
		self.helper.layout = Layout(
			Div(
				'title',
				'message',
				),
		)

# class Agreement(models.Model):
# 	user=models.ForeignKey(User)
# 	""" Daten für Teilnehmervereinbarung: """
# 	homeless = models.BooleanField(default=False)
# 	date_of_birth = models.DateField()
# 	GENDER_CHOICES = (
# 		('M', 'Männlich'),
# 		('W', 'Weiblich'),
# 	)
# 	sex = models.CharField(max_length=1,choices=GENDER_CHOICES)
# 	OCCUPATION_CHOICES = (
# 		('A','Arbeitslos gemeldet'),
# 		('B','Langzeitarbeitslos'),
# 		('C','Nicht Erwerbstätig'),
# 		('D','Keine Ausbildung'),
# 		('E','Erwerbstätig'),
# 	)
# 	job_A = models.BooleanField(default=False)
# 	job_B = models.BooleanField(default=False)
# 	job_C = models.BooleanField(default=False)
# 	job_D = models.BooleanField(default=False)
# 	job_E = models.BooleanField(default=False)
# 	AGE_GROUP_CHOICES = (
# 		('A','Jünger als 25'),
# 		('B','Älter als 54'),
# 		('C','Arbeitslos gemeldet'),
# 	)
# 	age_group = models.CharField(max_length=1,choices=AGE_GROUP_CHOICES)
# 	EDUCATION_CHOICES = (
# 		('A','ISCED 0'),
# 		('B','ISCED 1 -2'),
# 		('C','ISCED 3-4'),
# 		('D','ISCED 5-8'),
# 	)
# 	education = models.CharField(max_length=1,choices=EDUCATION_CHOICES)
# 	DOMESTIC_CHOICES = (
# 		('A','Erwerbslosenhaushalt'),
# 		('B','Kinder'),
# 		('C','Alleinerziehend'),
# 	)
# 	MIGRATION_CHOICES = (
# 		('A','Ja'),
# 		('B','Nein'),
# 		('C','Keine Angabe'),
# 	)
# 	migration = models.CharField(max_length=1,choices=MIGRATION_CHOICES)
# 	DISABILITY_CHOICES = (
# 		('A','Ja'),
# 		('B','Nein'),
# 		('C','Keine Angabe'),
# 	)
# 	disability = models.CharField(max_length=1,choices=DISABILITY_CHOICES)
# 	DISADVANTAGE_CHOICES = (
# 		('A','Ja'),
# 		('B','Nein'),
# 		('C','Keine Angabe'),
# 	)
# 	disadvantage = models.CharField(max_length=1,choices=DISADVANTAGE_CHOICES)
# 	date_added=models.DateField(default=timezone.now)