from django import forms
from ManageIdea.models import Idea
from ManageConnections.models import Announcement

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
				'description_short',
				'description_long',
				),
		)
		self.helper.form_tag = False
