from django.conf.urls import patterns, url

from ManageProjects import views

urlpatterns = patterns('',
    # ex: /users/sascha/
    url(r'^(?P<Project_id>\d+)/detail/$',views.detail, name='detail'),
    url(r'^(?P<Project_id>\d+)/edit/$',views.edit_project, name='edit_project'),
)
