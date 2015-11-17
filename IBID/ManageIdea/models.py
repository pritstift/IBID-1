import datetime
from django.db import models
from django.template.defaultfilters import title

from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin

from taggit.managers import TaggableManager

class Measure(models.Model):
	title=models.CharField(max_length=64, blank=False, unique=True)
	description_long=models.TextField(max_length=2048, blank=False)
	date_added=models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

class Idea(models.Model):
	title=models.CharField(max_length = 400, unique=True)
	originator = models.ForeignKey(User, default=False)
	secret = models.BooleanField(default=False)
	date_added=models.DateField(default=timezone.now)
	description_long=models.CharField(max_length=2048, blank=True, null=True)
	description_short=models.CharField(max_length=2048, blank=True, null=True)
	customer = models.CharField(max_length=2048, blank=True, null=True)
	problem=models.CharField(max_length=2048, blank=True, null=True)
	current_solution=models.CharField(max_length=2048,blank=True, null=True)
	gain=models.CharField(max_length=2048,blank=True, null=True)
	market_size=models.CharField(max_length=2048,blank=True, null=True)
	advantages=models.CharField(max_length=2048,blank=True, null=True)
	
	why_startup =models.CharField(max_length=2048, blank=True, null=True)
	why_now=models.CharField(max_length=2048,blank=True, null=True)
	motivation=models.CharField(max_length=2048,blank=True, null=True)
	support=models.CharField(max_length=2048, blank=True, null=True)

	status = models.CharField(max_length=2048, blank=True, null=True,)
	tags = TaggableManager(help_text="A comma-separated list of tags.")
	
	members = models.ManyToManyField(User, through='IdeaMembership', related_name='members')
	measures=models.ManyToManyField(Measure, through='IdeaMeasures')
	
	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)

	def __str__(self):
		return self.title



# Was ist die Geschäftsidee?
# •	Was ist das Angebot?
# •	An wen richtet sich dieses Angebot? (= Zielgruppe)
# •	Welches Problem löst das Angebot für die Zielgruppe?
# •	Wie löst aktuell die Zielgruppe das Problem? / Welche Aufwendungen hat die Zielgruppe, um das Problem zu lösen?
# •	Welchen Mehrwert bietet daher das neue Angebot für die Zielgruppe?
# •	Wie umfangreich ist der Markt? (qualitativ)
# •	Welche Vorteile bietet gerade die Geschäftsidee?
# •	Warum ist gerade ein Startup in der Lage diese Geschäftsidee zu realisieren?
# •	Warum ist gerade jetzt der richtige Zeitpunkt diese Geschäftsidee anzugehen?
# •	Was ist Eure Motivation?
# •	Wie kann Euch das TUGZ PT unterstützen?

			

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
	task = models.CharField(max_length=64, blank=True, null=True)
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


	
class IdeaMeasures(models.Model):
	measure=models.ForeignKey(Measure)
	idea=models.ForeignKey(Idea)
	start_date=models.DateField(blank=True, null=True)
	end_date=models.DateField(blank=True, null=True)
	date_added=models.DateTimeField(default=timezone.now)
	class Meta:
		unique_together=(
			'idea',
			'measure',
			)

