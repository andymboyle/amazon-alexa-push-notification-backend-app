from django.conf import settings

from django.conf.urls import url
from django.contrib import admin

import django.contrib.auth.views as auth_views
import django.views.static as static_views
import django.views.defaults as default_views

from django.contrib.auth.models import User

from rest_framework import routers

# api urls
router = routers.DefaultRouter(schema_title="Amazon Alexa Backend API")
router.register(r'content', ContentViewSet, base_name='content')
router.register(r'devices', DeviceViewSet, base_name='devices')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]