from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	
    url(r'^ideas/', include('ManageIdea.urls',namespace="ManageIdea")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('ManageUsers.urls', namespace="ManageUsers")),
)
