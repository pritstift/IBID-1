from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^ideas/', include('AddIdea.urls',namespace="AddIdea")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/upload.html$', 'AddIdea.views.post_upload', name='post_upload'),
     url(r'^post/(?P<post_id>\d+)/detail.html$',
    'AddIdea.views.post_detail', name='post_detail'),


)
