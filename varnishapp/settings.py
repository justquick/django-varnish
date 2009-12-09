manager = VarnishManager(*getattr(settings, 'VARNISH_MANAGMENT_ADDRS', ()))
