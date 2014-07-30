from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^programs/', include('programs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
