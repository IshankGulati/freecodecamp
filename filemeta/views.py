from django.views import View
from filemeta.forms import FileForm
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
import logging

logger = logging.getLogger('django')


class FileMetaView(View):
    def post(self, request, *args, **kwargs):
        MyFileForm = FileForm(request.POST, request.FILES)
        logger.error('entered view')
        if MyFileForm.is_valid():
            logger.error('success')
            filesize = MyFileForm.cleaned_data["fileupload"].size
            return JsonResponse({'size': filesize}, status=200)
        logger.error('failed')
        return HttpResponseBadRequest()