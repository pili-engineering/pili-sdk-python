"""
All api for access pili.
More Info: http://pili-io.github.io/docs/v1/index.html
"""
from .auth import auth_interface
import pili.conf as conf 
from urllib2 import Request
import json

@auth_interface
def create_stream(**args):
    print conf.API_HOST
    keyword = ['hub', 'title', 'publishKey', 'publishSecurity']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = "http://%s/%s/streams" % (conf.API_HOST, conf.API_VERSION)
    return Request(url=url, data=encoded)

@auth_interface
def get_stream(stream_id):
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url)

@auth_interface
def get_stream_list(**args):
    keyword = ['hub', 'marker', 'limit']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    url = "http://%s/%s/streams?" % (conf.API_HOST, conf.API_VERSION)
    for k in args:
        if args[k] != None:
            url += "&%s=%s" % (k, args[k])
    req = Request(url=url)
    return req

@auth_interface
def update_stream(stream_id, **args):
    keyword = ['publishKey', 'publishSecurity']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url, data=encoded)

@auth_interface
def delete_stream(stream_id):
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    req = Request(url=url)
    req.get_method = lambda: 'DELETE'
    return req

@auth_interface
def get_segments(stream_id, start_second, end_second):
    url = "http://%s/%s/streams/%s/segments?start=%s&end=%s" % (conf.API_HOST, conf.API_VERSION, stream_id, start_second, end_second)
    return Request(url=url)
