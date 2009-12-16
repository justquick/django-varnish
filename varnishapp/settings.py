from varnish import VarnishManager

manager = VarnishManager(*getattr(settings, 'VARNISH_MANAGMENT_ADDRS', ()))
