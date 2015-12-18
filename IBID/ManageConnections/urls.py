from django.conf.urls import patterns, url
from ManageConnections import views

urlpatterns = patterns('',
    # ex: /requests/5/post
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Request_id>\d+)/$', views.detail_announcement, name='detail_announcement'),
    url(r'^(?P<Request_id>\d+)/edit/$', views.edit_announcement, name='edit_announcement'),
    url(r'^(?P<Request_id>\d+)/remove/$', views.remove_announcement, name='remove_announcement'),
    url(r'^(?P<Membership_id>\d+)/edit/$', views.edit_membership, name='edit_membership'),
)
