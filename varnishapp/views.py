from django.http import HttpResponseRedirect
from manager import manager
from django.views.generic.simple import direct_to_template
from django.conf import settings

def get_stats():
    stats = [x[0] for x in manager.run('stats')]
    return zip(getattr(settings, 'VARNISH_MANAGEMENT_ADDRS', ()), stats)
    
def management(request): 
    if not request.user.is_superuser:
        return HttpResponseRedirect('/admin/')
    if 'command' in request.REQUEST:
        kwargs = dict(request.REQUEST.items())
        manager.run(*str(kwargs.pop('command')).split(), **kwargs)
        return HttpResponseRedirect(request.path)
    try:
        stats = get_stats()
        errors = {}
    except:
        stats = None
        errors = {"stats":"Impossible to access the stats for server : %s" \
                  %getattr(settings, 'VARNISH_MANAGEMENT_ADDRS', ())}
        
    extra_context = {'stats':stats,
                     'errors':errors}
    return direct_to_template(request, template='varnish/report.html',
                              extra_context=extra_context)
