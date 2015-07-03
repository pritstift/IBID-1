from django import forms
from ManageIdea.models import Idea
from ManageConnections.models import AnnounceIdea, AnnounceUser


class AnnounceIdeaForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = AnnounceIdea
		exclude = ['owner','date_added','idea']

class AnnounceUserForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = AnnounceUser
		exclude = ['owner','date_added']
