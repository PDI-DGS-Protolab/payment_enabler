from django.conf.urls import patterns, include, url

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^payment_info$', 'payment.views.payment_info'),
    url(r'^acquire$', 'payment.views.initial_payment'),

    url(r'^gw/adyen$', 'payment.adyen.callback.callback'),

    url(r'^gw/worldpay/success$', 'payment.worldpay.callback.success'),
    url(r'^gw/worldpay/pending$', 'payment.worldpay.callback.pending'),
    url(r'^gw/worldpay/error$',   'payment.worldpay.callback.error'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
)
