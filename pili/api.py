"""
All api for access pili.
More Info: http://pili-io.github.io/docs/v1/index.html
"""
from .auth import auth_interface
from .settings import API_HOST, API_VERSION
from urllib2 import Request
import json

@auth_interface
def create_stream(**args):
    keyword = ['stream_key', 'comment', 'is_private']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = API_HOST + API_VERSION + '/streams'
    req = Request(url=url, data=encoded)
    return req

@auth_interface
def get_stream(stream_id):
    url = API_HOST + API_VERSION + '/streams/' + stream_id
    req = Request(url=url)
    return req

@auth_interface
def get_stream_list():
    url = API_HOST + API_VERSION + '/streams'
    req = Request(url=url)
    return req

@auth_interface
def update_stream(stream_id, **args):
    keyword = ['stream_key', 'comment', 'is_private']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = API_HOST + API_VERSION + '/streams/' + stream_id
    req = Request(url=url, data=encoded)
    return req

@auth_interface
def delete_stream(stream_id):
    url = API_HOST + API_VERSION + '/streams/' + stream_id
    req = Request(url=url)
    req.get_method = lambda: 'DELETE'
    return req

@auth_interface
def get_stream_status(stream_id):
    url = API_HOST + API_VERSION + '/streams/' + stream_id + '/status'
    req = Request(url=url)
    return req

@auth_interface
def get_segments(stream_id, starttime, endtime):
    url = (API_HOST +
           API_VERSION +
           '/streams/%s/segments?starttime=%s&endtime=%s' % (stream_id, starttime, endtime))
    req = Request(url=url)
    return req

@auth_interface
def delete_segments(stream_id, starttime, endtime):
    url = (API_HOST +
           API_VERSION +
           '/streams/%s/segments?starttime=%s&endtime=%s' % (stream_id, starttime, endtime))
    req = Request(url=url)
    req.get_method = lambda: 'DELETE'
    return req

