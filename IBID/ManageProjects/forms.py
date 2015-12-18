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
		self.fields['active'].label = "Aktiv"

		