# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('twitter_oauth.oauth.views',
    # Top Page
    url(r'^oauth/$', 'index', name='index'),
    # Twitter OAuth Authenticate
    url(r'^oauth/get/$', 'get', name='get'),
    # Callback
    url(r'^oauth/get_callback/$', 'get_callback', name='get_callback'),
    # Redirect Page of after Authenticate
    url(r'^oauth/oauth_index/$', 'oauth_index', name='oauth_index'),
    # Tweet
    url(r'^oauth/post/$', 'post', name='post'),
)
