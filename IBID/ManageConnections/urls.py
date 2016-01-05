from django.conf.urls import patterns, url, include
from ManageConnections import views

urlpatterns = patterns('',
    # ex: /conn/5/post
    url(r'^$', views.index, name='index'),
    url(r'^announcement/(?P<Request_id>\d+)/$', views.detail_announcement, name='detail_announcement'),
)
