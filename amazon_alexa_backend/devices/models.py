from __future__ import unicode_literals

from django.db import models

class AmazonDevice(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)
    user_id = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return "%s:%s" % (self.type, self.user_id)