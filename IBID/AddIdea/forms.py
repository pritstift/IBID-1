from django import forms
from AddIdea.models import Idea

class PostForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Idea
		fields=['title', 'description_short','description_long','tags']

