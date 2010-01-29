from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^docs/$', 'api.views.docindex'),
    (r'^docs/(?P<command>\w+)/$', 'api.views.docs'),

    (r'^product_show/$', 'api.views.product_show'),
    (r'^product_add/$', 'api.views.product_add'),
    (r'^product_delete/$', 'api.views.product_delete'),
    (r'^uptake/$', 'api.views.uptake'),
)

