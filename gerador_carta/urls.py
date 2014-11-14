from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^texto/(?P<id>\d+)/$', 'gerador.views.gera_texto', name='texto'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(admin.site.urls)),
)
