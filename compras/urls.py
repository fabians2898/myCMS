from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from main.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compras.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.compras', name ='compras'),
    url(r'^clientes/', 'main.views.clientes', name ='clientes'),
    url(r'^sedes/', 'main.views.sedes', name ='sedes'),
    url(r'^productos/', 'main.views.productos', name ='productos'),


)
