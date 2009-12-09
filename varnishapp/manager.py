from varnish import VarnishManager
from django.conf import settings
from atexit import register


manager = VarnishManager(*getattr(settings, 'VARNISH_MANAGMENT_ADDRS', ()))
register(manager.close)