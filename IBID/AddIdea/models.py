import datetime

from django.utils import timezone
from django.db import models

class User(models.Model):
    name=models.CharField(max_length=256, unique=True)
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.CharField(max_length=256, unique=True)
    def __str__(self):
        return self.name

class Group(models.Model):
    name=models.CharField(max_length=256, unique=True)
    members=models.ManyToManyField(User, through='Membership')
    def __str__(self):
        return self.name

class Membership(models.Model):
    user=models.ForeignKey(User)
    group=models.ForeignKey(Group)

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
    tags=models.ForeignKey(Tag)
    def __str__(self):
        return self.title
