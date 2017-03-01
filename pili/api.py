from .auth import auth_interface
import pili.conf as conf
from urllib2 import Request
import json
import base64


def normalize(args, keyword):
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    for k, v in args.items():
        if v is None:
            del args[k]
    return args


@auth_interface
def create_stream(hub, **kwargs):
    keyword = ['key']
    encoded = json.dumps(normalize(kwargs, keyword))
    url = "http://%s/%s/hubs/%s/streams" % (conf.API_HOST, conf.API_VERSION, hub)
    return Request(url=url, data=encoded)


@auth_interface
def get_stream(hub, key):
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url)


@auth_interface
def get_stream_list(hub, **kwargs):
    keyword = ['liveonly', 'prefix', 'limit', 'marker']
    args = normalize(kwargs, keyword)
    url = "http://%s/%s/hubs/%s/streams?" % (conf.API_HOST, conf.API_VERSION, hub)
    for k, v in args.items():
        url += "&%s=%s" % (k, v)
    return Request(url=url)


@auth_interface
def batch_live_status(hub, streams):
    encoded = json.dumps({"items": streams})
    url = "http://%s/%s/hubs/%s/livestreams?" % (conf.API_HOST, conf.API_VERSION, hub)
    return Request(url=url, data=encoded)


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
def stream_saveas(hub, key, **kwargs):
    keyword = ['start', 'end', 'fname', 'format', 'pipeline', 'notify', 'expireDays']
    encoded = json.dumps(normalize(kwargs, keyword))
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/saveas" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url, data=encoded)


@auth_interface
def stream_snapshot(hub, key, **kwargs):
    keyword = ['time', 'fname', 'format']
    encoded = json.dumps(normalize(kwargs, keyword))
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/snapshot" % (conf.API_HOST, conf.API_VERSION, hub, key)
    return Request(url=url, data=encoded)


@auth_interface
def get_history(hub, key, **kwargs):
    keyword = ['start', 'end']
    args = normalize(kwargs, keyword)
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/historyactivity?" % (conf.API_HOST, conf.API_VERSION, hub, key)
    for k, v in args.items():
        url += "&%s=%s" % (k, v)
    return Request(url=url)


@auth_interface
def update_stream_converts(hub, key, profiles):
    key = base64.urlsafe_b64encode(key)
    url = "http://%s/%s/hubs/%s/streams/%s/converts" % (conf.API_HOST, conf.API_VERSION, hub, key)
    encoded = json.dumps({"converts": profiles})
    return Request(url=url, data=encoded)
