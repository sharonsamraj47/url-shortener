from django.conf import settings
from django_hosts import patterns, host
#from kirr.hostsconf import urls as redirect_urls

host_patterns = patterns('',
    host("www", settings.ROOT_URLCONF, name="www"),
    host("www", "kirr.hostsconf.urls", name="wildcard"),
)