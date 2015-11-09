from django import forms
from ManageIdea.models import Idea, IdeaPrivacy, Comment, IdeaMembership, IdeaMeasures
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions, InlineRadios

from ManageUsers.models import UserProfile
from django.contrib.auth.models import User

from guardian.shortcuts import assign_perm, get_perms, remove_perm

from datetimewidget.widgets import DateWidget



class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		exclude = ['owner','date_added', 'members', 'measures']
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'title',
				'description_short',
				'description_long',
				'status',
				'ressources',
				'tags',
				css_class="tab-pane active",
				css_id="description",
				role="tabpanel" ,
				),
			Div(
				'pictures',
				'files',
				css_class="tab-pane",
				css_id="files",
				role="tabpanel" ,
				),
		)
		self.helper.form_tag = False

class PrivacyForm(forms.ModelForm):
	class Meta:
		model = IdeaPrivacy
		exclude = ['instance']
	def __init__(self, *args, **kwargs):
		super(PrivacyForm,self).__init__(*args, **kwargs)
		self.fields['description_long_ip'].label = "Description long"
		self.fields['tags_ip'].label = "Tags"
		self.fields['status_ip'].label = "Status"
		self.fields['ressources_ip'].label = "Ressources"
		self.fields['pictures_ip'].label = "Pictures"
		self.fields['files_ip'].label = "Files"
		self.fields['members_ip'].label = "Members"
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				HTML("<b>What information should be public? </b>"),
				'description_long_ip',
				'tags_ip',
				'status_ip',
				'ressources_ip',
				'pictures_ip',
				'files_ip',
				'members_ip',
				css_class="tab-pane",
				css_id="privacy",
				role="tabpanel" ,
				),
			)
		self.helper.form_tag = False

class DisplayIdeaForm(forms.ModelForm):
	class Meta:
		model = Idea
		exclude = ['owner', 'date_added']
	def __init__(self, *args, **kwargs):
		super(DisplayIdeaForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			self.fields['title'].widget.attrs['readonly'] = True
			self.fields['description_short'].widget.attrs['readonly'] = True
			self.fields['description_long'].widget.attrs['readonly'] = True
			self.fields['status'].widget.attrs['readonly'] = True
			self.fields['ressources'].widget.attrs['readonly'] = True
			self.fields['tags'].widget.attrs['readonly'] = True
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'title',
				'description_short',
				'description_long',
				'status',
				'ressources',
				'tags',
				css_class="tab-pane active",
				css_id="description",
				role="tabpanel" ,
				),
		)

class CommentForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	visible = forms.BooleanField( required=False, initial=False)
	class Meta:
		model = Comment
		exclude = ['supervisor', 'date_added','idea']
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.fields['title'].label = "Title"
		self.fields['message'].label = "Message"
		self.fields['visible'].label = "Visble to idea owner?"
		self.helper.layout = Layout(
			Div(
				'title',
				'message',
				'visible',
				),
		)

class AddMemberForm(forms.ModelForm):
	username = forms.CharField(required=True)
	can_edit = forms.BooleanField(required=False, initial = False)
	class Meta:
		model = IdeaMembership
		exclude = ['idea', 'member', 'date_added']
	
	def __init__(self, *args, **kwargs):
		super(AddMemberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['username'].label = "Username"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Allow this user to edit the idea?"
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
		model = IdeaMembership
		exclude = ['idea', 'date_added']
	
	def __init__(self, *args, **kwargs):
		super(EditMemberForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['member'].label = "User"
		self.fields['task'].label = "Task"
		self.fields['can_edit'].label = "Allow this user to edit the idea?"
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

class AddIdeaMeasureForm(forms.ModelForm):
	class Meta:
		model = IdeaMeasures
		exclude=['idea', 'date_added']
		widgets = {
		'start_date': DateWidget(attrs={'id':"start_date_id"}, usel10n = True, bootstrap_version=3),
		'end_date': DateWidget(attrs={'id':"end_date_id"}, usel10n = True, bootstrap_version=3)
		}

	def __init__(self,*args, **kwargs):
		super(AddIdeaMeasureForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['measure'].label = "Measure"
		self.fields['start_date'].label = "Start Date"
		self.fields['end_date'].label = "End Date"
		self.helper.form_tag = False
		self.helper.layout = Layout(
			Div(
				'measure',
				'start_date',
				'end_date',
				),
			)
	def clean_end_date(self):
		
		start_date = self.cleaned_data.get('start_date')
		end_date = self.cleaned_data.get('end_date')
		if end_date:
			if start_date:
				if end_date < start_date:
					raise forms.ValidationError('The start date must be earlier than the end date ')
			else:
				raise forms.ValidationError('Leave empty or provide a start date ')    			
		return end_date
