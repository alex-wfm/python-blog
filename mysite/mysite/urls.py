from django.conf.urls import patterns, include, url

from mysite.views import *



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        ('^$', myHomepageView),
        ('^hello/$', hello),
        ('^time/$', current_datetime),
        (r'^time/plus/(?P<offset>\d{1,2})/$', hours_ahead),
        (r'^time/plus2/(?P<offset>\d{1,2})/(?P<param2>\d{1,2})/$', test_param_ext),
        (r'^admin/', include(admin.site.urls)),
                       
                       
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
