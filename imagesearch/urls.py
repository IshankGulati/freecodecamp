from django.conf.urls import url
from imagesearch.views import ImageSearchView, SearchHistoryView, IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="img_search_index"),
    url(r'imagesearch/(?P<query>[a-zA-z0-9\s]+)/$', ImageSearchView.as_view(), name="imagesearch"),
    url(r'latest/$', SearchHistoryView.as_view(), name="searchhistory"),
]