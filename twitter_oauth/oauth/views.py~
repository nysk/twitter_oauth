# Create your views here.
# -*- coding:utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

import tweepy

CONSUMER_KEY = 'Q7nC6CKzaTy2RhxgLtUOGQ'
CONSUMER_SECRET = 'd6ZTP6kOMt5IfdiWROps0mnXPIgpSHpdrTIjNorhQ'
CALLBACK_URL = 'http://127.0.0.1:8000/oauth/get_callback/'


def index(request):
    '''
    Top Page
    '''
    return render_to_response('oauth/index.html')


def get(request):
    '''
    Twitter OAuth Authenticate
    '''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)

    try:
        auth_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    request.session['request_token'] = (auth.request_token.key, auth.request_token.secret)
    return HttpResponseRedirect(auth_url)


def get_callback(request):
    '''
    Callback
    '''
    # Example using callback (web app)
    verifier = request.GET.get('oauth_verifier')

    # Let's say this is a web app, so we need to re-build the auth handler first...
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    token = request.session.get('request_token')
    del request.session['request_token']
    auth.set_request_token(token[0], token[1])

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    request.session['key'] = auth.access_token.key
    request.session['secret'] = auth.access_token.secret
    return HttpResponseRedirect(reverse('twitter_oauth.oauth.views.oauth_index'))


def oauth_index(request):
    '''
    Redirect Page of after Authenticate 
    '''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(request.session.get('key'), request.session.get('secret'))
    api = tweepy.API(auth_handler=auth)

    # Get username
    username = auth.get_username()

    # Get timeline
    timeline_list = api.home_timeline()

    ctxt = RequestContext(request, {
            'username': username,
            'timeline_list': timeline_list,
            })
    return render_to_response('oauth/oauth_index.html', ctxt)


def post(request):
    '''
    Tweet
    '''
    if request.method == 'POST':
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(request.session.get('key'), request.session.get('secret'))
        api = tweepy.API(auth_handler=auth)

        tweet = request.POST["tweet"]
        api.update_status(tweet)
        return HttpResponse('Tweet complete!!')
