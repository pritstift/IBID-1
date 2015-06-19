from django import forms
from ManageIdea.models import Idea

class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		fields=['title', 'description_short','description_long','description_long_ip','tags','tags_ip']

