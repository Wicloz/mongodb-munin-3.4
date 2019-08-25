#!/usr/bin/env python

from os import environ
import pymongo
try:
    import urllib.parse as urlparse
except ImportError:
    import urllib as urlparse

url = ''
if 'mongourl' in environ:
    url = environ['mongourl']

if url == '':
    socket = ''
    if 'mongosocket' in environ:
        socket = urlparse.quote_plus(environ['mongosocket'])

    host = '127.0.0.1'
    if 'mongohost' in environ:
        host = environ['mongohost']

    port = 27017
    if 'mongoport' in environ:
        port = int(environ['mongoport'])

    user = ''
    if 'mongouser' in environ:
        user = urlparse.quote_plus(environ['mongouser'])

    password = ''
    if 'mongopassword' in environ:
        password = urlparse.quote_plus(environ['mongopassword'])

    authsource = 'admin'
    if 'mongoauthsource' in environ:
        authsource = environ['mongoauthsource']

    if password == '' and user == '':
        urlstart = 'mongodb://'
        urlend = ''
    else:
        urlstart = 'mongodb://%s:%s@' % (user, password)
        urlend = '/%s' % (authsource)

    if socket != '':
        url = urlstart + socket + urlend
    else:
        url = urlstart + host + ":" + str(port) + urlend

def getServerStatus(conn_timeout_secs = 30):
    client = pymongo.MongoClient(url, serverSelectionTimeoutMS=(conn_timeout_secs * 1000))
    return client.admin.command('serverStatus', rangeDeleter=True, repl=True)

def getListDatabases(conn_timeout_secs = 30):
    client = pymongo.MongoClient(url, serverSelectionTimeoutMS=(conn_timeout_secs * 1000))
    return client.admin.command('listDatabases')
