from django.conf.urls import patterns, url

from ManageIdea import views
from ManageConnections.views import post_announcement

urlpatterns = patterns('',
    # ex: /Ideas/
    url(r'^$', views.index, name='index'),
    # ex: /Ideas/5/
    url(r'^post/$', views.post, name='post'),
    url(r'^edit/(?P<Idea_id>\d+)/$', views.edit, name='edit'),
    url(r'^request/post/(?P<Idea_id>\d+)/$', post_announcement, name='post_announcement'),
    url(r'^(?P<Idea_id>\d+)/$', views.detail, name='detail'),
)
