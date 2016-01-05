from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from ManageIdea.models import Idea
from ManageUsers.models import UserProfile

class ProjectState(models.Model):
    """
    Description: Projektstatus
    """
    title = models.CharField(max_length = 256, unique = True)
    description = models.CharField(max_length = 2048, blank=True, null=True)
    APPEARANCECHOICELIST = (
    		('default','Default'),
    		('primary','Primary'),
    		('info','Info'),
    		('success','Success'),
    		('warning','Warning'),
    		('danger','Danger'),
    	)
    appearance = models.CharField(max_length = 7, choices=APPEARANCECHOICELIST, default = 'default')
    date_added = models.DateField(default = timezone.now)
    def __str__(self):
    	return self.title
    

class Project(models.Model):
	"""
	Description: project class
	"""
	title = models.CharField(max_length = 256, unique=True)
	description = models.CharField(max_length = 2048, blank=True, null=True)
	status = models.ForeignKey(ProjectState, null=True, blank = True)
	date_added = models.DateField(default = timezone.now)

	members = models.ManyToManyField(User, through = 'ProjectGroup')
	ideas = models.ManyToManyField(Idea, through = 'ProjectIdeas')

	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)

	def __str__(self):
		return self.title


	
class ProjectGroup(models.Model):
	"""
	Description: Projektgruppe
	"""
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	date_joined = models.DateField(default = timezone.now)
	tasks = models.CharField(max_length = 256)

	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)
		unique_together = (
			'project',
			'user',
			)

class ProjectIdeas(models.Model):
	"""
	Description: Welche Ideen gehören zu dem Projekt?
	"""
	idea = models.ForeignKey(Idea)
	project = models.ForeignKey(Project)
	date_added = models.DateField(default = timezone.now)

	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)
		unique_together = (
			'project',
			'idea',
			)