from django.conf.urls import patterns, url
from ManageConnections import views

urlpatterns = patterns('',
    # ex: /requests/5/post
    url(r'^(?P<Idea_id>\d+)/post_request$', views.post_idea_request, name='post_idea_request'),
    url(r'^(?P<Request_id>\d+)/detail_idea_request$', views.detail_idea_request, name='detail_idea_request'),
    url(r'^(?P<User_name>\w+)/post_request$', views.post_user_request, name='post_user_request'),
    url(r'^(?P<Request_id>\d+)/detail_user_request$', views.detail_user_request, name='detail_user_request'),
)
