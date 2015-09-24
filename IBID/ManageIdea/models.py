import datetime
from django.db import models
from django.template.defaultfilters import title

from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin

from taggit.managers import TaggableManager


class Idea(models.Model):
	title=models.CharField(max_length = 400, unique=True)
	owner = models.ForeignKey(User, related_name='owner')
	date_added=models.DateField(default=timezone.now)
	description_short=models.CharField(max_length=2048, blank=True)
	description_long=models.CharField(max_length=2048, blank=True)
	status = models.CharField(max_length=2048, blank=True)
	tags = TaggableManager(help_text="A comma-separated list of tags.")
	ressources = models.CharField(max_length=2048, blank=True)
	pictures = models.ImageField(upload_to='pictures', blank=True)
	files = models.FileField(upload_to='idea_files', blank=True)
	members = models.ManyToManyField(User, through='IdeaMembership', related_name='members')
	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)


	def __str__(self):
		return self.title
		

class IdeaPrivacy(models.Model):
	instance = models.ForeignKey(Idea)
	description_long_ip = models.BooleanField(default=False)
	tags_ip = models.BooleanField(default=False)
	status_ip = models.BooleanField(default=False)
	ressources_ip = models.BooleanField(default=False)
	pictures_ip = models.BooleanField(default=False)
	files_ip = models.BooleanField(default=False)
	members_ip = models.BooleanField(default=False)
	comments_ip = models.BooleanField(default=False)
	def __str__(self):
		return self.instance.title

class Comment(models.Model):
	supervisor = models.ForeignKey(User)                   # User mit staffpermission
	idea = models.ForeignKey(Idea)
	title=models.CharField(max_length=64,blank=False, default='')
	message = models.TextField(blank=False)
	date_added = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title
	class Meta:
		permissions = (
			('view', 'View Comment'),
			('edit', 'Edit Comment'),
		)

class IdeaMembership(models.Model):
	idea = models.ForeignKey(Idea)
	member = models.ForeignKey(User)
	task = models.CharField(max_length=64, blank=True, default='')
	date_added = models.DateTimeField(default = timezone.now)
	class Meta:
		permissions = (
			('view', 'View Membership'),
			('edit', 'Edit Membership'),
		)
		unique_together = (
			'idea',
			'member',
			)