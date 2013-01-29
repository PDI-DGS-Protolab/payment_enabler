from django.conf.urls import patterns, include, url

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # payment data acquisition API
    url(r'^acquire/service$',             'payment_gateways.views.acquire_service'),
    url(r'^acquire/form/(?P<token>\w+)$', 'payment_gateways.views.acquire_form'),
    url(r'^acquire/redirect$',            'payment_gateways.views.acquire_redirect'),

    # recurrent payment API
    url(r'^recurrent$', 'payment_gateways.views.recurrent_payment'),
    
    # adyen callback API
    url(r'^gw/adyen$', 'payment_gateways.adyen.callback.callback'),

    # worldpay callback API
    url(r'^gw/worldpay/success$', 'payment_gateways.worldpay.callback.success'),
    url(r'^gw/worldpay/pending$', 'payment_gateways.worldpay.callback.pending'),
    url(r'^gw/worldpay/error$',   'payment_gateways.worldpay.callback.error'),

    # serving static content from development server
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
)
