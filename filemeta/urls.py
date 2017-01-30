from django.conf.urls import url
from django.views.generic import TemplateView
from filemeta.views import FileMetaView


urlpatterns = [
    url(r'^filesize/$', FileMetaView.as_view(), name="filemeta"),
    url(r'^$', TemplateView.as_view(template_name="partials/filemeta/filemeta.form.html"), name="filemetaview"),
]