import datetime
from django.db import models
from django.template.defaultfilters import title

from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

# class Group(models.Model):
#     name=models.CharField(max_length=256, unique=True)
#     members=models.ManyToManyField(User, through='Membership')
#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     user=models.ForeignKey(User)
#     group=models.ForeignKey(Group)

class Tag(models.Model):
    text=models.CharField(max_length=64)
    def __str__(self):
        return self.text


class Idea(models.Model):
    title=models.CharField(max_length = 400, unique=True)
    owner = models.ForeignKey(User)
    date_added=models.DateField(default=timezone.now())
    description_short=models.CharField(max_length=2048,default="this Idea has no short description yet")
    description_long=models.CharField(max_length=2048,default="this Idea has no long description yet")
    description_long_ip=models.BooleanField(default=False)
    tags = TaggableManager(help_text="A comma-separated list of tags.")
    tags_ip = models.BooleanField(default=False)
    
    class Meta:
        permissions = (
            ('view_idea', 'View idea'),
        )

    def __str__(self):
        return self.title
                                                                                                                               
                                                                                          
class Comment(models.Model):
    user = models.ForeignKey(User)                                                                  
    idea = models.ForeignKey(Idea)                                                             
    message = models.TextField(blank=False)                                                               
    created_at = models.DateTimeField(default=timezone.now())

