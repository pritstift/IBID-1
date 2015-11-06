from django.conf.urls import patterns, url

from ManageIdea import views
from ManageConnections.views import post_announcement, edit_announcement, remove_announcement

urlpatterns = patterns('',
	# ex: /Ideas/
	url(r'^$', views.index, name='index'),
	# ex: /Ideas/5/
	url(r'^post/', views.post, name='post_idea'),
	url(r'^post/(?P<User_id>\d+)/', views.post, name='post'),
	url(r'^edit/(?P<Idea_id>\d+)/$', views.edit, name='edit'),
	url(r'^addmember/(?P<Idea_id>\d+)/$', views.addmember, name='add_member'),
	url(r'^editmember/(?P<Membership_id>\d+)/$', views.editmember, name='edit_member'),
	url(r'^addmeasure/(?P<Idea_id>\d+)/$', views.add_idea_measure, name='add_idea_measure'),
	url(r'^editmeasure/(?P<Measure_id>\d+)/$', views.edit_measure, name='edit_measure'),
	url(r'^removemeasure/(?P<Measure_id>\d+)/$', views.remove_measure, name='remove_measure'),
	url(r'^removemember/(?P<Membership_id>\d+)/$', views.removemember, name='remove_member'),
	url(r'^request/post/(?P<Idea_id>\d+)/$', post_announcement, name='post_announcement'),
	url(r'^request/edit/(?P<Idea_id>\d+)/(?P<Request_id>\d+)/$', edit_announcement, name='edit_announcement'),
	url(r'^request/remove/(?P<Idea_id>\d+)/(?P<Request_id>\d+)/$', remove_announcement, name='remove_announcement'),
	url(r'^(?P<Idea_id>\d+)/$', views.detail, name='detail'),
	url(r'^comment/(?P<Idea_id>\d+)/$', views.createcomment, name='createcomment'),
	url(r'^editcomment/(?P<Comment_id>\d+)/$', views.editcomment, name='edit_comment'),
	url(r'^removecomment/(?P<Comment_id>\d+)/$', views.removecomment, name='remove_comment'),
)
