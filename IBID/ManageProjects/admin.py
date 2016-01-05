from django.contrib import admin
from ManageProjects.models import Project, ProjectGroup, ProjectState
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectGroup)
admin.site.register(ProjectState)