from django import forms
from ManageIdea.models import Idea
from ManageConnections.models import Announcement, Membership

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions, InlineRadios


class AnnouncementForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Announcement
		exclude = ['owner','date_added','idea']
	def __init__(self, *args, **kwargs):
		super(AnnouncementForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'title',
				'description_long',
				),
		)
		self.helper.form_tag = False

class AddMemberForm(forms.ModelForm):
	username = forms.CharField(required=True)
	can_edit = forms.BooleanField(required=False, initial = False)
	class Meta:
		model = Membership
		exclude = ['idea','project', 'member', 'date_added']
	
	def __init__(self, *args, **kwargs):
		super(AddMemberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['username'].label = "Username"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Kann Instanz editieren"
		self.helper.layout = Layout(
			Div(
				'username',
				'task',
				'can_edit'
				),
			FormActions(
				Submit('save', 'Submit'),
			),
		)

	def clean_username(self):
		username=self.cleaned_data.get('username')

		if not User.objects.filter(username=username).count():
			raise forms.ValidationError('There is no user with that username')
		
		if IdeaMembership.objects.filter(member=User.objects.get(username=username)).count():
			raise forms.ValidationError('You already added this user')
		return username

class EditMemberForm(forms.ModelForm):
	can_edit = forms.BooleanField(required=False, initial = False)
	class Meta:
		model = Membership
		exclude = ['idea','project', 'date_added']
	
	def __init__(self, *args, **kwargs):
		super(Membership, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['member'].label = "User"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Kann Instanz editieren"
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'member',
				readonly="readonly",
				),
			Div(
				'task',
				'can_edit',
				),
		)