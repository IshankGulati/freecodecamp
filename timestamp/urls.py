from django.conf.urls import url
from timestamp.views import IndexView, TimestampView

urlpatterns = [
    url(r'(?P<timest>[0-9a-zA-Z,\s]+)/$', TimestampView.as_view(), name="timestamp"),
    url(r'^$', IndexView.as_view(), name='timestampIndex'),
]
