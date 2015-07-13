from django.conf.urls import patterns, url

from ManageUsers import views
from ManageConnections.views import post_announcement
urlpatterns = patterns('',
    # ex: /users/sascha/
    url('^login/',views.user_login, name='login'),
    url('^logout/','django.contrib.auth.views.logout',{'next_page':'/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/(?P<User_id>\d+)/$', views.edit, name='edit'),
    url(r'^request/post/(?P<User_id>\d+)/$', post_announcement, name='post_announcement'),
    url(r'^(?P<User_id>\d+)/$', views.userprofile, name='userprofile'),
)
