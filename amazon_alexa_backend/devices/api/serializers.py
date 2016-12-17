# -*- coding: utf-8 -*-
import logging
import requests

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.db.models import Model
from django.template import loader

from ..models import AmazonDevice

from rest_framework import serializers


class AmazonDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AmazonDevice
        fields = (
            'created_on',
            'type',
            'user_id',
            'pk',
        )

    def get_type(self, obj):
    	return obj.type

    def get_user_id(self, obj):
        return obj.user_id

    def get_created_on(self, obj):
    	return obj.created_on

    def get_pk(self, obj):
    	return obj.pk