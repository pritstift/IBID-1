from django import forms
 
class PostForm(forms.Form):
    content = forms.CharField(max_length=1000)
    created_at = forms.DateTimeField()

'''
Created on Mar 15, 2015

@author: SRAONE
'''
