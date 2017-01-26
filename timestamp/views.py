from django.views.generic.base import TemplateView
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.http import JsonResponse

import datetime
import time
import logging


logger = logging.getLogger('django')

# Create your views here.
class IndexView(TemplateView):
    template_name = "partials/timestamp/timestamp.html"

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class TimestampView(View):
    def get(self, request, timest):
        unixt = None
        normt = None

        converted = False
        logger.info(timest)
        try:
            dt = datetime.datetime.strptime(str(timest), '%B %d, %Y')
        except:
            logger.error('Not normal date')
        else:
            unixt = time.mktime(dt.timetuple())
            normt = dt.strftime('%B %d, %Y')
            converted = True

        if not converted:
            try:
                normt = datetime.datetime.utcfromtimestamp(float(timest)).strftime(
                    '%B %d, %Y')
            except:
                logger.error('Not unix date')
            else:
                unixt = timest

        return JsonResponse({"unix": unixt, "natural": normt})


