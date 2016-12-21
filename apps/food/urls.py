# -*- coding: utf-8 -*-
from django.conf.urls import url
from .viewsets import UploadMenuAPIView

urlpatterns = [
    url(r'^upload/$', UploadMenuAPIView.as_view(), name="upload_menu")
]
