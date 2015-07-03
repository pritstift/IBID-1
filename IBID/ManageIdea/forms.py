from django import forms
from ManageIdea.models import Idea, StatusRelationship, Status


class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		exclude = ['owner','date_added']

class StatusForm(forms.ModelForm):
	species=forms.ChoiceField(StatusRelationship.CHOICES)
	status=Status.objects.all()
	class Meta:
		model = StatusRelationship
		fields = ['species']
