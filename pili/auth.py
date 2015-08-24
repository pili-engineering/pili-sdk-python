"""
Auth provide class Auth for authentication account. You can use decorator
auth_interface to create a function with auto generated authentication.
"""
import pili.conf as conf
from urlparse import urlparse
from .utils import send_and_decode, __hmac_sha1__

class Credentials(object):
    def __init__(self, access_key, secret_key):
        if not (access_key and secret_key):
            raise ValueError('invalid key')
        self.__auth__ = Auth(access_key, secret_key)

class Auth(object):
    """
    class Auth store the access_key and secret_key for authentication.
    """
    def __init__(self, access_key, secret_key):
        if not (access_key and secret_key):
            raise ValueError('invalid key')
        self.__access_key, self.__secret_key = access_key, secret_key

    def auth_interface_str(self, raw_str):
        """
        generate sign str.
        """
        encoded = __hmac_sha1__(raw_str, self.__secret_key)
        return 'Qiniu {0}:{1}'.format(self.__access_key, encoded)

def auth_interface(method):
    """
    decorator takes func(**args) return req and change it to
    func(auth, **args) return json result.

    Args:
        func(**args) -> Request

    Returns:
        func(**args) -> dict (decoded json)
    """
    def authed(auth, **args):
        """
        send request and decode response. Return the result in python format.
        """
        req = method(**args)
        parsed = urlparse(req.get_full_url())
        raw_str = '%s %s' % (req.get_method(), parsed.path)
        if parsed.query:
            raw_str += '?%s' % (parsed.query)
        raw_str += '\nHost: %s' % (parsed.netloc)
        if req.has_data():
            raw_str +=  '\nContent-Type: application/json'
        raw_str+="\n\n"
        if req.has_data():
            raw_str += req.get_data()
            req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', auth.auth_interface_str(raw_str))
        return send_and_decode(req)
    return authed

