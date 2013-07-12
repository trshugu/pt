# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^item/(?P<item_id>\d+)/$', 'apptmp.views.item_page_display'),
    # Examples:
    # url(r'^$', 'djangotmp.views.home', name='home'),
    # url(r'^djangotmp/', include('djangotmp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
