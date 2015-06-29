from django.contrib import admin
from ManageIdea.models import Idea, Status, statusRelationship, StatusAdmin

admin.site.register(Idea)
admin.site.register(Status, StatusAdmin)
# Register your models here.
