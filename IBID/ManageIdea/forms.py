from django import forms
from ManageIdea.models import Idea, StatusRelationship, Status


class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		#fields=['title', 'description_short','description_long','description_long_ip','tags','tags_ip']
		exclude = [field.name for field in Idea._meta.fields if not '_ip' in field.name]+['owner','date_added']

class StatusForm(forms.ModelForm):
	#species=forms.ChoiceField(StatusRelationship.CHOICES)
	status=Status.objects.all()
	class Meta:
		model = StatusRelationship
		fields = ['species']
