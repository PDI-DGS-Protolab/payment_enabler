from django.conf.urls import patterns, include, url

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'payment.views.initial_payment'),

    url(r'^success$', 'payment.views.success'),
    url(r'^pending$', 'payment.views.pending'),
    url(r'^error$',   'payment.views.error'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
)
