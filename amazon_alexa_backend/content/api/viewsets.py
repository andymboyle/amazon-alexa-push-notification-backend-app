import json

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import F

from ..models import Content

from rest_framework import viewsets, permissions, status as statuses
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from .serializers import ContentSerializer
from .filters import ContentFilter

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_class = ContentFilter
    # permission_classes = (permissions.DjangoModelPermissions, )