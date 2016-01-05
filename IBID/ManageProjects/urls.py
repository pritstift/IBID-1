from django.conf.urls import patterns, url

from ManageProjects import views
from ManageConnections.views import addmember

urlpatterns = patterns('',
    # ex: /users/sascha/
    url(r'^(?P<Project_id>\d+)/detail/$',views.detail, name='detail'),
    url(r'^(?P<Project_id>\d+)/edit/$',views.edit_project, name='edit_project'),
    url(r'^(?P<Project_id>\d+)/add_member/$',addmember, name='addmember'),
)
