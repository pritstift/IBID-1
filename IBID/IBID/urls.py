from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^ideas/', include('AddIdea.urls',namespace="AddIdea")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('ManageUsers.urls', namespace="ManageUsers")),
)
