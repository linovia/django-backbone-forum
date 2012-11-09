from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_backbone_todo.views.home', name='home'),
    # url(r'^django_backbone_todo/', include('django_backbone_todo.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('django_backbone_todo.todo.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
)
