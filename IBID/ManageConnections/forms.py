from django import forms
# import autocomplete_light.shortcuts as autocomplete_light
from django.contrib.auth.models import User
from ManageIdea.models import Idea
from ManageProjects.models import Project
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
	# member = autocomplete_light.ModelChoiceField('UserAutocomplete')
	project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.HiddenInput())
	idea = forms.ModelChoiceField(queryset=Idea.objects.all(), widget=forms.HiddenInput())
	class Meta:
		model = Membership
		exclude = ['date_added']
	
	def __init__(self, *args, **kwargs):
		super(AddMemberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['member'].label = "Nutzer"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Kann Instanz editieren"
		self.helper.layout = Layout(
			Div(
				'member',
				'task',
				'can_edit',
				'project',
				'idea',
				),
			FormActions(
				Submit('save', 'Submit'),
			),
		)

	def clean_member(self):
		member = self.cleaned_data.get('member')
		idea = self.cleaned_data.get('idea')
		project = self.cleaned_data.get('project')
		# idea = self.__dict__["fields"]["idea"]
		# project = self.__dict__["fields"]["project"]
		print('vlidation')
		print(project,idea)
		if idea is not None:
			if Membership.objects.filter(member=member,idea=idea).count():
				raise forms.ValidationError('Dieser Nutzer ist bereits Mitglied im Ideenpapier')
		elif project is not None:
			print(Membership.objects.filter(member=member,project=project).count())
			if Membership.objects.filter(member=member,project=project).count():
				raise forms.ValidationError('Dieser Nutzer ist bereits Mitglied im Projekt')
		return member

class EditMemberForm(forms.ModelForm):
	class Meta:
		model = Membership
		exclude = ['idea','project', 'date_added']
	
	def __init__(self, *args, **kwargs):
		super(EditMemberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['member'].label = "User"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Kann editieren"
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