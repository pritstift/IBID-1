from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateWidget

# from ManageIdea.models import Idea, IdeaPrivacy, Comment, IdeaMembership, IdeaMeasures
# from ManageUsers.models import UserProfile
from ManageProjects.models import Project, ProjectGroup

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions, InlineRadios, Accordion, AccordionGroup
from guardian.shortcuts import assign_perm, get_perms, remove_perm

class ProjectForm(forms.ModelForm):
	"""Form zum anlegen einer Projektgruppe"""
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Project
		exclude =['date_added','members', 'ideas']
	def __init__(self, *args,**kwargs):
		super(ProjectForm, self).__init__(*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.fields['title'].label = "Name des Projekts"
		self.fields['description'].label = "Kurze Beschreibung"
		self.fields['status'].label = "Aktiv"


# class AddIdeaMeasureForm(forms.ModelForm):
# 	class Meta:
# 		model = IdeaMeasures
# 		exclude=['idea', 'date_added']
# 		widgets = {
# 		'start_date': DateWidget(attrs={'id':"start_date_id"}, usel10n = True, bootstrap_version=3),
# 		'end_date': DateWidget(attrs={'id':"end_date_id"}, usel10n = True, bootstrap_version=3)
# 		}

# 	def __init__(self,*args, **kwargs):
# 		super(AddIdeaMeasureForm, self).__init__(*args, **kwargs)
# 		self.helper = FormHelper()
# 		self.fields['measure'].label = "Measure"
# 		self.fields['start_date'].label = "Start Date"
# 		self.fields['end_date'].label = "End Date"
# 		self.helper.form_tag = False
# 		self.helper.layout = Layout(
# 			Div(
# 				'measure',
# 				'start_date',
# 				'end_date',
# 				),
# 			)
# 	def clean_end_date(self):
		
# 		start_date = self.cleaned_data.get('start_date')
# 		end_date = self.cleaned_data.get('end_date')
# 		if end_date:
# 			if start_date:
# 				if end_date < start_date:
# 					raise forms.ValidationError('The start date must be earlier than the end date ')
# 			else:
# 				raise forms.ValidationError('Leave empty or provide a start date ')    			
# 		return end_date