from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	company = models.CharField(max_length=256,blank=True)
	occupation = models.CharField(max_length=256, blank=True)
	website = models.URLField(blank=True)
	phone_number = models.CharField(max_length=15,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."),], blank=True) # validators should be a list
	email_adress = models.EmailField(max_length=254)
	date_joined = models.DateField(default=timezone.now)
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
	phone_number_ip = models.BooleanField(default=False)
	company_ip = models.BooleanField(default=False)
	occupation_ip = models.BooleanField(default=False)
	website_ip = models.BooleanField(default=False)
	email_adress_ip = models.BooleanField(default=False)
