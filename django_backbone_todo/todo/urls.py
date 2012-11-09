from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ThreadList, ThreadDetail, MessageList, MessageDetail
from .views import api_root

urlpatterns = patterns('',
    url(r'^$', api_root),
    url(r'^threads/$', ThreadList.as_view(), name='thread-list'),
    url(r'^threads/(?P<pk>\d+)/$', ThreadDetail.as_view(), name='thread-detail'),
    url(r'^messages/$', MessageList.as_view(), name='message-list'),
    url(r'^messages/(?P<pk>\d+)/$', MessageDetail.as_view(), name='message-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
