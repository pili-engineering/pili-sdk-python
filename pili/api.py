from .auth import auth_interface
import pili.conf as conf
from urllib2 import Request
import json, base64

def normalize(args, keyword):
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    for k, v in args.items():
        if v is None:
            del args[k]
    return args


@auth_interface
def create_stream(hub, **args):
    keyword = ['key']
    encoded = json.dumps(normalize(args, keyword))
    url = "http://%s/%s/hubs/%s/streams" % (conf.API_HOST, conf.API_VERSION, hub)
    return Request(url=url, data=encoded)

@auth_interface
def get_stream(hub, key):
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url)

@auth_interface
def get_stream_list(hub, **args):
    keyword = ['liveonly', 'prefix', 'limit', 'marker']
    args = normalize(args, keyword)
    url = "http://%s/%s/hubs/%s/streams?" % (conf.API_HOST, conf.API_VERSION, hub)
    for k, v in args.items():
        url += "&%s=%s" % (k, v)
    req = Request(url=url)
    return req

@auth_interface
def disable_stream(hub, key, till):
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/disabled" % (conf.API_HOST, conf.API_VERSION, hub, key)
    encoded = json.dumps({"disabledTill": till})
    return Request(url=url, data=encoded)

@auth_interface
def get_status(hub, key):
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/live" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url)

@auth_interface
def save_stream_as(hub, key, **args):
    keyword = ['start', 'end']
    encoded = json.dumps(normalize(args, keyword))
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/saveas" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url, data=encoded)

@auth_interface
def get_history(hub, key, **args):
    keyword = ['start', 'end']
    encoded = json.dumps(normalize(args, keyword))
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/historyactivity" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url, data=encoded)
