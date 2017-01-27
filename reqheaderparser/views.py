from django.views import View
from django.http import JsonResponse

import re


class ClientInfoView(View):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        lang = request.META.get('HTTP_ACCEPT_LANGUAGE')

        user_agent = request.META.get('HTTP_USER_AGENT')
        ua_split = re.split(r'\(|\)|\*|\n', user_agent)

        return JsonResponse({
            "ipaddress": ip,
            "language": lang,
            "software": ua_split[1],
        })
