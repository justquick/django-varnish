from django.conf.urls.defaults import *
from django.conf import settings
from manager import VarnishManager


urlpatterns = patterns('varnishapp.views',
    (r'', 'management'),
)
