from django.conf.urls import patterns, url

from ManageUsers import views

urlpatterns = patterns('',
    # ex: /users/sascha/
    url(r'^profile/(?P<User_username>\w+)/$', views.userprofile, name='userprofile'),
    url('^login/','django.contrib.auth.views.login', name='login'),
    url('^logout/','django.contrib.auth.views.logout',{'next_page':'AddIdea:index'}, name='logout'),
)
