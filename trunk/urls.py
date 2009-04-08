# coding=utf-8
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^overseas/', include('overseas.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'overseas.index.main'),
    (r'^login/$', 'overseas.login.views.login'),
    (r'^logout/$', 'overseas.login.views.logout'),
    (r'^home/$', 'overseas.home.views.main'),
    (r'^resource/$', 'overseas.home.views.resource'),
    (r'^about/$', 'overseas.home.views.about'),
    (r'^news/((?P<n_id>\w+)/)?$', 'overseas.home.views.news'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_PATH}),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
