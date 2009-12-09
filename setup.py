from distutils.core import setup

setup(
    name = "django-varnish",
    version = '0.1',
    url = 'http://opensource.washingtontimes.com/projects/django-varnish/',
    author = 'Justin Quick',
    description = 'Integration between Django and the Varnish HTTP accelerator using the management port using telnet',
    packages = ['varnishapp']
)

