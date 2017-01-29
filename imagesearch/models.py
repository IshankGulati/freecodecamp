from __future__ import unicode_literals

from django.db import models


class ImageSearchModel(models.Model):
    query = models.CharField(max_length=50, null=False)
    created_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.query