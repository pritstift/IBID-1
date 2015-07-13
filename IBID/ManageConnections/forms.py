from django import forms
from ManageIdea.models import Idea
from ManageConnections.models import Announcement


class AnnouncementForm(forms.ModelForm):
	description_long = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Announcement
		exclude = ['owner','date_added','idea']
