"""
Auth provide class Auth for authentication account. You can use decorator
auth_interface to create a function with auto generated authentication.
More Information:
http://pili-io.github.io/docs/v1/index.html?shell#jie-kou-jian-quan
"""
import hmac, hashlib, base64
from urlparse import urlparse
from .utils import send_and_decode
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
        encoded = self.__hmac_sha1(raw_str, self.__secret_key)
        return 'pili {0}:{1}'.format(self.__access_key, encoded)

    @staticmethod
    def __hmac_sha1(data, key):
        """
        hmac-sha1
        """
        hashed = hmac.new(key, data, hashlib.sha1)
        return base64.urlsafe_b64encode(hashed.digest())


def auth_interface(method):
    """
    decorator takes func(**args) return req and change it to
    func(auth, **args) return json result.

    Args:
        func(**args) -> Request

    Returns:
        func(auth, **args) -> dict (decoded json)
    """
    def authed(auth, **args):
        """
        send request and decode response. Return the result in python format.
        """
        req = method(**args)
        parsed = urlparse(req.get_full_url())
        raw_str = parsed.path
        if parsed.query:
            raw_str += '?%s' % (parsed.query)
        raw_str += '\n'
        if req.has_data():
            raw_str += req.get_data()
        req.add_header('Authorization', auth.auth_interface_str(raw_str))
        req.add_header('Content-Type', 'application/json')
        return send_and_decode(req)
    return authed

