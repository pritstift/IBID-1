from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    company = models.CharField(max_length=256,blank=True)
    company_ip = models.BooleanField(default=False)
    occupation = models.CharField(max_length=256, blank=True)
    occupation_ip = models.BooleanField(default=False)
    website = models.URLField(blank=True)
    website_ip = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    picture_ip = models.BooleanField(default=False)
    files = models.FileField(upload_to='idea_files', blank=True)
    files_ip = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now())
    # Override the __unicode__() method to return out something meaningful!
    class Meta:
        permissions = (
            ('view', 'View UserProfile'),
            ('edit', 'Edit UserProfile'),
        )
    def __unicode__(self):
        return self.user.username
