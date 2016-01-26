from django.conf.urls import patterns, url

from ManageUsers import views
from ManageConnections.views import post_announcement, edit_announcement, remove_announcement
from ManageProjects.views import create_project
urlpatterns = patterns('',
    # ex: /users/sascha/
    url('^login/',views.user_login, name='login'),
    url('^logout/','django.contrib.auth.views.logout',{'next_page':'/'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/(?P<User_id>\d+)/$', views.edit, name='edit'),
    url(r'^edit/(?P<User_id>\d+)/ability/$', views.edit_ability, name='edit_ability'),
    url(r'^comment/(?P<User_id>\d+)/$', views.createcomment, name='createcomment'),
    url(r'^comment/edit/(?P<Comment_id>\d+)$', views.editcomment, name='editcomment'),
    url(r'^comment/remove/(?P<Comment_id>\d+)$', views.removecomment, name='removecomment'),
    url(r'^(?P<User_id>\d+)/request/post/$', post_announcement, name='post_announcement'),
    url(r'^(?P<User_id>\d+)/request/edit/(?P<Request_id>\d+)$', edit_announcement, name='edit_announcement'),
    url(r'^(?P<User_id>\d+)/request/remove/(?P<Request_id>\d+)$', remove_announcement, name='remove_announcement'),
    url(r'^(?P<User_id>\d+)/project/create/$', create_project, name='create_project'),
    url(r'^(?P<User_id>\d+)/$', views.userprofile, name='userprofile'),
)
