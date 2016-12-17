import json

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import F

from ..models import AmazonDevice

from rest_framework import viewsets, permissions, status as statuses
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from .serializers import AmazonDeviceSerializer
from .filters import AmazonDeviceFilter

class AmazonDeviceViewSet(viewsets.ModelViewSet):
    queryset = AmazonDevice.objects.all()
    serializer_class = AmazonDeviceSerializer
    filter_class = AmazonDeviceFilter
    # permission_classes = (permissions.DjangoModelPermissions, )