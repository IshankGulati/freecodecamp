from django.views import View
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest, JsonResponse

import requests

from imagesearch.models import ImageSearchModel


class IndexView(TemplateView):
    template_name = "partials/imagesearch/imagesearch.html"

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class ImageSearchView(View):
    search_api = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"
    bing_key = "f78aec4dc9d64eb7a13589aa78147917"

    def get(self, request, query, *args, **kwargs):
        offset = request.GET.get('offset', 0)
        payload = {
            'q': query,
            'offset': offset
        }
        headers = {'Ocp-Apim-Subscription-Key': ImageSearchView.bing_key}

        req = requests.get(ImageSearchView.search_api, params=payload, headers=headers)

        if req.status_code != requests.codes.ok:
            return HttpResponseBadRequest()

        response = req.json()
        search_resp = []
        for image in response['value']:
            filtered_resp = {
                'snippet': image['name'],
                'url': image['contentUrl'],
                'thumbnail': image['thumbnailUrl'],
                'context': image['hostPageDisplayUrl']
            }
            search_resp.append(filtered_resp)

        search_obj = ImageSearchModel(query=query)
        search_obj.save()

        return JsonResponse(search_resp, status=200, safe=False)


class SearchHistoryView(View):
    def get(self, request, *args, **kwargs):
        queryset = ImageSearchModel.objects.order_by('-created_at')[:10]
        response = []
        for item in queryset:
            ser_item = {'query': item.query, 'created_at': item.created_at}
            response.append(ser_item)
        return JsonResponse(response, status=200, safe=False)