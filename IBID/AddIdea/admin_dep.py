from django.contrib import admin
from AddIdea.models import Idea, Tag

admin.site.register(Idea)
admin.site.register(Tag)
admin.site.unregister(User)
# Register your models here.
