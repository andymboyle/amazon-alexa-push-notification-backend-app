from ..models import Content

from rest_framework import filters


class ContentFilter(filters.FilterSet):
    class Meta:
        model = Content
        fields = [
            'text',
            'date'
        ]