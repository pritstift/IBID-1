from django.conf.urls import patterns, url

from ManageProjects import views
from ManageConnections.views import addmember, remove_membership, edit_membership

urlpatterns = patterns('',
    # ex: /users/sascha/
    url(r'^(?P<Project_id>\d+)/detail/$',views.detail, name='detail'),
    url(r'^(?P<Project_id>\d+)/edit/$',views.edit_project, name='edit_project'),
    url(r'^(?P<Project_id>\d+)/add_member/$',addmember, name='addmember'),
    url(r'^(?P<Project_id>\d+)/members/(?P<Membership_id>\d+)/edit$', edit_membership, name='edit_membership'),
	url(r'^(?P<Project_id>\d+)/members/(?P<Membership_id>\d+)/remove$', remove_membership, name='remove_membership'),
    url(r'^(?P<Project_id>\d+)/add_measure/$',views.add_measure, name='add_measure'),
    url(r'^(?P<Project_id>\d+)/create_note/$',views.create_note, name='create_note'),


)
