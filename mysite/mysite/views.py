'''
Created on Jun 2, 2013

@author: alex
'''
from django.http import HttpResponse, Http404
from django.template import Template, Context
import datetime

def hello(request):
    return HttpResponse("Hello world")

def myHomepageView (request) :
    return HttpResponse("Home Page")



# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)



def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def test_param_ext(request, *callback_args, **callback_kwargs):
    print "prams = ", callback_kwargs
    try:
        p1 = int(callback_kwargs["offset"])
        p2 = int(callback_kwargs["param2"])
        
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=p1)
    html = "<html><body>In %s hour(s), it will be %s.--param2 = %s</body></html>" % (p1, dt, p2)
    return HttpResponse(html)

def test () :
    print "test"
    

    
test()