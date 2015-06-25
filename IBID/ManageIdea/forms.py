from django import forms
from ManageIdea.models import Idea, statusRelationship, Status


class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		fields=['title', 'description_short','description_long','description_long_ip','tags','tags_ip']
		#exclude=['user','date_added']

class StatusForm(forms.ModelForm):
	species=forms.ChoiceField(statusRelationship.CHOICES)
	status=Status.objects.all()
	class Meta:
		model = statusRelationship
		fields = ['idea','species']
