from .auth import Auth, auth_interface
from .settings import API_HOST, API_VERSION
from urllib2 import Request 

@auth_interface
def create_stream(auth, **args):
    keyword = ['stream_key', 'comment', 'is_private']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = API_HOST + API_VERSION + '/streams'
    req = Request(url = url, data = encoded)
    return req

@auth_interface
def get_stream(auth, id):
    url = API_HOST + API_VERSION + '/streams/' + id
    req = Request(url = url)
    return req

@auth_interface
def get_stream_list(auth):
    url = API_HOST + API_VERSION + '/streams'
    req = Request(url = url)
    return req

@auth_interface
def update_stream(auth, id, **args):
    keyword = ['stream_key', 'comment', 'is_private']
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    encoded = json.dumps(args)
    url = API_HOST + API_VERSION + '/streams/' + id
    req = Request(url = url, data = encoded)
    return req

@auth_interface
def delete_stream(auth, id):
    url = API_HOST + API_VERSION + '/streams/' + id
    req = Request(url = url)
    req.get_method = lambda: 'DELETE'
    return req

@auth_interface
def get_stream_status(auth, id):
    url = API_HOST + API_VERSION + '/streams/' + id + '/status'
    req = Request(url = url)
    return req