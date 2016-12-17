from ..models import AmazonDevice

from rest_framework import filters


class AmazonDeviceFilter(filters.FilterSet):
    class Meta:
        model = AmazonDevice
        fields = [
            'user_id'
        ]