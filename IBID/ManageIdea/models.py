import datetime
from django.db import models
from django.template.defaultfilters import title

from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin

from taggit.managers import TaggableManager

# class Group(models.Model):
#     name=models.CharField(max_length=256, unique=True)
#     members=models.ManyToManyField(User, through='Membership')
#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     user=models.ForeignKey(User)
#     group=models.ForeignKey(Group)

#Titel
#Customer
#Kurzbeschreibung
#Beschreibung (is_public || has_customer_permission)
#Benötigte Ressourcen (is_public || has_ staff_permission)
#Fotos (is_public || has_ customer_permission)
#Dateien (is_public || has_ customer_permission)
#Score (is_public || has_ staff_permission)
#Betreuungsstatus (is_public || has_customer_permission || has_ staff_permission)
#Staff Kommentare (has_staff_permission)
#Staff Dateien (has_staff_permission)

class Idea(models.Model):
    title=models.CharField(max_length = 400, unique=True)
    owner = models.ForeignKey(User)
    date_added=models.DateField(default=timezone.now())
    description_short=models.CharField(max_length=2048,default="this Idea has no short description yet")
    description_long=models.CharField(max_length=2048,default="this Idea has no long description yet")
    description_long_ip=models.BooleanField(default=False)
    tags = TaggableManager(help_text="A comma-separated list of tags.")
    tags_ip = models.BooleanField(default=False)
    status_ip = models.BooleanField(default=False)
    ressources = models.CharField(max_length=2048,default="Any ressources in need?")
    ressources_ip = models.BooleanField(default=False)
    pictures = models.ImageField(upload_to='idea_images', blank=True)
    pictures_ip = models.BooleanField(default=False)
    files = models.FileField(upload_to='idea_files', blank=True)
    files_ip = models.BooleanField(default=False)
    #score = models.IntegerField(default=2)
    score_ip = models.BooleanField(default=False)
    #maintenanceStatus = models.ForeignKey(MaintenanceStatus)
    maintenanceStatus_ip = models.BooleanField(default=False)
    class Meta:
        permissions = (
            ('view_idea', 'View idea'),
        )

    def __str__(self):
        return self.title

class Status(models.Model):
    title = models.CharField(max_length = 400, unique=True)
    ideas = models.ManyToManyField(Idea, through='StatusRelationship')
    date_added=models.DateField(default=timezone.now())
    def __str__(self):
        return self.title

class StatusRelationship(models.Model):
    CHOICES = (
    ('EMPTY', ''),
    ('FINISHED', 'Abgeschlossen'),
    ('CURRENT', 'Aktiv'),
    )
    idea = models.ForeignKey(Idea)
    status = models.ForeignKey(Status)
    date_added = models.DateField(default=timezone.now())
    species = models.CharField(max_length=10,choices=CHOICES,default='EMPTY')
    def __str__(self):
        return self.species

class StatusRelationshipInline(admin.TabularInline):
    model = StatusRelationship
    extra = 2 # how many rows to show

class StatusAdmin(admin.ModelAdmin):
    inlines = (StatusRelationshipInline,)



#class Ressources(models.Model):
#    idea = models.ForeignKey(Idea)
#    title = models.CharField(max_length = 400, unique=True)
#    date_added = models.DateTimeField(default=timezone.now())

class MaintenanceStatus(models.Model):
    supervisor = models.ManyToManyField(User)              # User mit staffpermission
    idea = models.ForeignKey(Idea)
    title = models.CharField(max_length = 400, unique=True)
    date_added = models.DateTimeField(default=timezone.now())

class Comment(models.Model):
    supervisor = models.ForeignKey(User)                   # User mit staffpermission
    idea = models.ForeignKey(Idea)
    message = models.TextField(blank=False)
    date_added = models.DateTimeField(default=timezone.now())
