from varnish import VarnishManager
from django.conf import settings


manager = VarnishManager(*getattr(settings, 'VARNISH_MANAGMENT_ADDRS', ()))
