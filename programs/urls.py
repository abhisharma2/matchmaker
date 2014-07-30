from django.conf.urls import patterns, url

from programs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^matrix/$', views.matrix, name='matrix'),
    url(r'^finder/$', views.finder, name='finder'),
    url(r'^hypothetical/$', views.hypothetical, name='hypothetical')
)
