from django.conf.urls import patterns, url

from AddIdea import views

urlpatterns = patterns('',
    # ex: /Ideas/
    url(r'^$', views.index, name='index'),
    # ex: /Ideas/5/
    url(r'^(?P<Idea_id>\d+)/$', views.detail, name='detail'),
    )
