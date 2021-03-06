from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('app.views',
    url(r'^$','show_authentication_page'),
    url(r'^show/$','showlog'),
    url(r'^debug/$', 'showdebug'),
    url(r'^json/domain/$','ajax_getDomainInfo'),
    url(r'^json/domain/(?P<_days>\d+)/$','ajax_getDomainInfo'),
    url(r'^json/countryStats/$','ajax_getCountryInfo_days'),
    url(r'^json/countryStats/(?P<_days>\d+)/$','ajax_getCountryInfo_days'),
    url(r'^json/logInfo/$', 'ajax_getLogInfo'),
    url(r'^add/$', 'insertlog'),
)
        
