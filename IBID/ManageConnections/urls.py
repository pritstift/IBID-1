from django.conf.urls import patterns, url
from ManageConnections import views

urlpatterns = patterns('',
    # ex: /requests/5/post
    url(r'^(?P<Idea_id>\d+)/post$', views.post_idea_request, name='post_idea_request'),
    url(r'^(?P<Idea_id>\d+)/(?P<Request_id>\d+)/detail$', views.detail_idea_request, name='detail_idea_request'),
)
