from django import forms
from ManageIdea.models import Idea, StatusRelationship, Status, IdeaPrivacy
from IBID.functions import get_ip_fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions



class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		exclude = ['owner','date_added']
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'title',
				'description_short',
				'description_long',
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

class StatusForm(forms.ModelForm):
	species=forms.ChoiceField(StatusRelationship.CHOICES)
	class Meta:
		model = StatusRelationship
		fields = ['species']
	def __init__(self, *args, **kwargs):
		super(StatusForm,self).__init__(*args, **kwargs)
		self.status=Status.objects.all()
		self.helper=FormHelper()
		divlist=[]
		for status in self.status:
			divlist.append(
				Div(
					HTML(status),
					Field('species'),
					)
				)
		self.helper.layout=Layout(
				Div(
					*divlist
					),
			)
		self.helper[0].wrap(Div,css_id="status",role="tabpanel" , css_class="tab-pane")
		self.helper.form_tag = False
		self.helper.form_show_labels = False

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
		self.helper=FormHelper()
		self.helper.layout=Layout(
			Div(
				'description_long_ip',
				'tags_ip',
			    'status_ip',
			    'ressources_ip',
			    'pictures_ip',
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
