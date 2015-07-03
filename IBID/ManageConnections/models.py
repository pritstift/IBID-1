from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from ManageIdea.models import Idea
from ManageUsers.models import UserProfile
# Create your models here.


class AnnounceIdea(models.Model):
    title = models.CharField(max_length = 400, unique=True)
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea)
    date_added = models.DateField(default=timezone.now())
    description_short=models.CharField(max_length=2048,default="this request has no short description yet")
    description_long=models.CharField(max_length=2048,default="this request has no long description yet")
    class Meta:
        permissions = (
            ('view', 'View AnnounceIdea'),
        )
        
class AnnounceUser(models.Model):
    title = models.CharField(max_length = 400, unique=True)
    owner = models.ForeignKey(User)
    date_added = models.DateField(default=timezone.now())
    description_short=models.CharField(max_length=2048,default="this request has no short description yet")
    description_long=models.CharField(max_length=2048,default="this request has no long description yet")
