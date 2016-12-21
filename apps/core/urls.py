# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import LandingPageTemplateView
from .viewsets import JarvisAPIView

urlpatterns = [
    url(r'^$', LandingPageTemplateView.as_view(), name='landing'),
    url(r'^endpoint/$', JarvisAPIView.as_view(), name="jarvis_home")
]
