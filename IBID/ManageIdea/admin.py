from django.contrib import admin

from ManageIdea.models import Idea, IdeaMembership

from guardian.admin import GuardedModelAdmin

from functools import partial

class IdeaMembershipInline(admin.TabularInline):
	model = IdeaMembership
	extra=1


class IdeaAdmin(GuardedModelAdmin):
	fields = ['title', 'owner','date_added', 'description_short','description_long']
	ordering = ('-date_added',)
	inlines = (IdeaMembershipInline,)
	@property
	def queryset(self):
		return partial(self.get_queryset)


admin.site.register(Idea,IdeaAdmin)
admin.site.register(IdeaMembership)

# Register your models here.
