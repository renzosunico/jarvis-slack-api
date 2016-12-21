# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    """Site landing page."""

    template_name = 'core/landing_page.html'
