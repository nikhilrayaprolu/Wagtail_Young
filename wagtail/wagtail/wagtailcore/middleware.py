from __future__ import absolute_import, unicode_literals

import django
from wagtail.wagtailcore.models import Site


if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
else:
    MiddlewareMixin = object


class SiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """
        Set request.wagsite to contain the Site object responsible for handling this request,
        according to hostname matching rules
        """
        try:
            request.wagtailsite = Site.find_for_request(request)
        except Site.DoesNotExist:
            request.wagtailsite = None
