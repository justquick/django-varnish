from django.conf.urls.defaults import *
from django.conf import settings
from managers import VarnishManager

def get_stats():
    stats = [x[0] for x in manager.run('stats')]
    return zip(getattr(settings, 'VARNISH_MANAGEMENT_ADDRS', ()), stats)

urlpatterns = patterns('django.views.generic.simple',
    (r'', 'direct_to_template', {'template':'varnish/report.html', 'extra_context': {'stats':get_stats}}),
)
