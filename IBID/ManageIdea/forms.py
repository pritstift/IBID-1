from django import forms
from ManageIdea.models import Idea, IdeaPrivacy, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, HTML, MultiField, Field
from crispy_forms.bootstrap import FormActions, InlineRadios, Accordion, AccordionGroup

from ManageUsers.models import UserProfile
from django.contrib.auth.models import User

from guardian.shortcuts import assign_perm, get_perms, remove_perm

from datetimewidget.widgets import DateWidget



class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	description_short = forms.CharField(widget=forms.Textarea)
	customer = forms.CharField(widget=forms.Textarea, required=False)
	problem = forms.CharField(widget=forms.Textarea, required=False)
	current_solution = forms.CharField(widget=forms.Textarea, required=False)
	gain = forms.CharField(widget=forms.Textarea, required=False)
	market_size = forms.CharField(widget=forms.Textarea, required=False)
	advantages = forms.CharField(widget=forms.Textarea, required=False)
	why_startup = forms.CharField(widget=forms.Textarea, required=False)
	why_now = forms.CharField(widget=forms.Textarea, required=False)
	motivation = forms.CharField(widget=forms.Textarea, required=False)
	support = forms.CharField(widget=forms.Textarea, required=False)
	status = forms.CharField(widget=forms.Textarea, required=False)
	class Meta:
		model = Idea
		exclude = ['originator','date_added', 'members', 'measures']
	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.helper=FormHelper()
		self.fields['title'].label ="Titel des Ideenpapiers"
		self.fields['tags'].label = "Stichworte"
		self.fields['secret'].label = "Die Idee unterliegt strenger Geheimhaltung"
		self.fields['description_long'].label = "Was ist die Geschäftsidee?"
		self.fields['description_short'].label = "Was ist das Angebot?"
		self.fields['customer'].label = "An wen richtet sich das Angebot?(=Zielgruppe)"
		self.fields['problem'].label = "Welches Probem löst die Idee für die Zielgruppe?"
		self.fields['current_solution'].label = "Wie löst die Zielgruppe aktuell dieses Problem?"
		self.fields['gain'].label = "Welchen Mehrwehrt bietet das neue Angebot für die Zielgruppe?"
		self.fields['market_size'].label = "Wie umfangreich ist der Markt (qualitativ)?"
		self.fields['advantages'].label = "Welchen Mehrwehrt bietet gerade diese Geschäftsidee?"
		self.fields['why_startup'].label = "Warum ist gerade ein Startup in der Lage diese Geschäftsidee zu realisieren?"
		self.fields['why_now'].label = "Warum ist gerade jetzt der richtige Zeitpunkt für die Geschäftsidee?"
		self.fields['motivation'].label = "Was ist die Motivation?"
		self.fields['support'].label = "Wie kann das TUGZ unterstützen?"
		self.fields['status'].label = "Was ist der aktuelle Status der Geschäftsidee?"
		# self.helper.form_class = 'form-inline'
		# self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout=Layout(
			Div(
				Accordion(
    				AccordionGroup(
    					'Beschreibung',
						Div(
							Div(
								'title',
								css_class="col-md-8",
							),
							Div(
								'secret',
								css_class="col-md-4",
							),
							css_class="row",
						),
						Div(
							Div(
								'tags',
								css_class="col-md-12",
							),
							css_class="row",
						),
						Div(
							Div(
								'description_long',
								css_class="col-md-6",
							),
							Div(
								'description_short',
								css_class="col-md-6",
							),
							css_class="row",
						),
					),
					AccordionGroup(
						'Zielgruppe und Markt',
						Div(
							Div(
								'customer',
								css_class="col-md-6",
							),
							Div(
								'problem',
								css_class="col-md-6",
							),
							css_class="row",
						),
						Div(
							Div(
								'current_solution',
								css_class="col-md-6",
							),
							Div(
								'gain',
								css_class="col-md-6",
							),
							css_class="row",
						),
						Div(
							Div(
								'market_size',
								css_class="col-md-6",
							),
							Div(
								'advantages',
								css_class="col-md-6",
							),
							css_class="row",
						),
					),
					AccordionGroup(
						'Sonstiges',
						Div(
							Div(
								'why_startup',
								css_class="col-md-6",
							),
							Div(
								'why_now',
								css_class="col-md-6",
							),
							css_class="row",
						),
						Div(
							Div(
								'status',
								css_class="col-md-6",
							),
							Div(
								'motivation',
								css_class="col-md-6",
							),
							css_class="row",
						),
						Div(
							Div(
								'support',
								css_class="col-md-12",
							),
							css_class="row",
						),
					),
				),
				
				
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



