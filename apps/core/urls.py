# -*- coding: utf-8 -*-
from django.conf.urls import url
from core.views import LandingPageTemplateView

urlpatterns = [
    url(r'', LandingPageTemplateView.as_view(), name='landing'),
]
