from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator


class UserType(models.Model):
	title = models.CharField(max_length=32)
	description = models.CharField(max_length=256)
	date_added = models.DateField(default=timezone.now)
	def __str__(self):
		return self.title
		


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	company = models.CharField(max_length=256,blank=True)
	website = models.URLField(blank=True)
	phone_number = models.CharField(max_length=15,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),], blank=True) # validators should be a list
	street = models.CharField(max_length=256, blank=True, null=True)
	house_number = models.IntegerField(blank=True, null=True)
	zip_code = models.IntegerField(blank=True, null=True)
	city = models.CharField(max_length=256, blank=True, null=True)
	user_type = models.ForeignKey(UserType, blank=True, null=True)
	date_joined = models.DateField(default=timezone.now)
	# Override the __unicode__() method to return out something meaningful!
	class Meta:
		permissions = (
			('view', 'View UserProfile'),
			('edit', 'Edit UserProfile'),
		)
	def __str__(self):
		return self.user.username

class UserProfilePrivacy(models.Model):
	instance = models.ForeignKey(UserProfile)
	phone_number_ip = models.BooleanField(default=False)
	company_ip = models.BooleanField(default=False)	
	website_ip = models.BooleanField(default=False)
	email_adress_ip = models.BooleanField(default=False)
	street_ip = models.BooleanField(default=False)
	house_number_ip = models.BooleanField(default=False)
	zip_code_ip = models.BooleanField(default=False)
	city_ip = models.BooleanField(default=False)
	user_type_ip = models.BooleanField(default=False)

class UserActivation(models.Model):
	user = models.OneToOneField(User)
	code = models.CharField(max_length=20, blank=False)
	completed = models.BooleanField( default=False)	
	class Meta:
		verbose_name = "UserActivation"
		verbose_name_plural = "UserActivations"

	def __str__(self):
		pass

class UserComment(models.Model):
	supervisor = models.ForeignKey(User, related_name='supervisor')                   # User mit staffpermission
	user = models.ForeignKey(User, related_name='user')
	title=models.CharField(max_length=256, blank=False, default='')
	message = models.TextField(blank=False)
	date_added = models.DateTimeField(default=timezone.now)
	class Meta:
		permissions = (
			('view', 'View Idea'),
			('edit', 'Edit Idea'),
		)

	def __str__(self):
		return self.title