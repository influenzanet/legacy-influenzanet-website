from django.conf.urls.defaults import patterns,url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.feedback, name='feedback_index'),                    
    url(r'^maps/$', views.maps, name='feedback_maps'),
    url(r'^friend/$', views.tell_a_friend, name='feedback_tell_friend'),
)