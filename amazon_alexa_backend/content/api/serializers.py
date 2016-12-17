# -*- coding: utf-8 -*-
import logging
import requests

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.db.models import Model
from django.template import loader

from ..models import Content

from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonDevice
        fields = (
            'date',
            'text',
        )

    def get_date(self, obj):
        return obj.type

    def get_text(self, obj):
        return obj.user_id