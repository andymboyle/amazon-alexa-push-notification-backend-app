from __future__ import unicode_literals
import logging
import urlparse
from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.timezone import now
import requests


class Content(models.Model):
    text = models.TextField(max_length=500)
    slug = models.SlugField(max_length=140)
    date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.content

