from django.contrib import admin
from ManageIdea.models import Idea, Status, StatusRelationship

admin.site.register(Idea)
admin.site.register(Status)
admin.site.register(StatusRelationship)
# Register your models here.
