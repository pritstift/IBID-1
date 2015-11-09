from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from ManageIdea.models import Idea
from ManageUsers.models import UserProfile
# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length = 400, unique=True)
    owner = models.ForeignKey(User)
    idea = models.ForeignKey(Idea, blank=True, null=True)
    date_added = models.DateField(default=timezone.now)
    description_long=models.CharField(max_length=2048,default="this request has no long description yet")
    class Meta:
        permissions = (
            ('view', 'View Announcement'),
            ('edit', 'Edit Announcement'),
        )

    def __str__(self):
        return self.title