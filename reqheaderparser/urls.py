from django.conf.urls import url
from reqheaderparser.views import ClientInfoView

urlpatterns = [
    url(r'^$', ClientInfoView.as_view(), name="clientinfo"),
]