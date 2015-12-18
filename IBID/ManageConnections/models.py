from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from ManageUsers.models import UserProfile
# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length = 400, unique=False)
    owner = models.ForeignKey(User)
    idea = models.ForeignKey('ManageIdea.Idea', blank=True, null=True)
    date_added = models.DateField(default=timezone.now)
    description_long=models.CharField(max_length=2048,default="this request has no long description yet")
    class Meta:
        permissions = (
            ('view', 'View Announcement'),
            ('edit', 'Edit Announcement'),
        )

    def __str__(self):
        return self.title

class Membership(models.Model):
    """
    Description: This is a through model for Memberships, refers to Projects or Ideas
    """
    idea = models.ForeignKey('ManageIdea.Idea', blank=True, null=True)
    project = models.ForeignKey('ManageProjects.Project', blank=True, null=True)
    member = models.ForeignKey(User)
    task = models.CharField(max_length=64, blank=True, null=True)
    date_added = models.DateTimeField(default = timezone.now)
    class Meta:
        permissions = (
            ('view', 'View Membership'),
            ('edit', 'Edit Membership'),
        )
        unique_together = (
            (
                'idea',
                'member',
            ),
            (
                'project',
                'member',
            ),
            )