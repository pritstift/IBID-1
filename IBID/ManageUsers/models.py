from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    company = models.CharField(max_length=256,blank=True)
    occupation = models.CharField(max_length=256, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    files = models.FileField(upload_to='idea_files', blank=True)
    date_joined = models.DateField(default=timezone.now())
    # Override the __unicode__() method to return out something meaningful!
    class Meta:
        permissions = (
            ('view', 'View UserProfile'),
            ('edit', 'Edit UserProfile'),
        )
    def __unicode__(self):
        return self.user.username

class UserProfilePrivacy(models.Model):
    instance = models.ForeignKey(UserProfile)
    company_ip = models.BooleanField(default=False)
    occupation_ip = models.BooleanField(default=False)
    website_ip = models.BooleanField(default=False)
    picture_ip = models.BooleanField(default=False)
    files_ip = models.BooleanField(default=False)
