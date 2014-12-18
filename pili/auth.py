import hmac, hashlib, base64
from urlparse import urlparse
from .utils import send_and_decode

class Auth(object):

    def __init__(self, access_key, secret_key):
        if not (access_key and secret_key):
            raise ValueError('invalid key')
        self.__access_key, self.__secret_key = access_key, secret_key

    def auth_interface_str(self, raw_str):
        encoded = self.__hmac_sha1(raw_str, self.__secret_key)
        return 'pili {0}:{1}'.format(self.__access_key, encoded)

    @staticmethod
    def __hmac_sha1(data, key):
            hashed = hmac.new(key, data, hashlib.sha1)
            return base64.urlsafe_b64encode(hashed.digest())


def auth_interface(method):
    def authed(auth, **args):
        req = method(auth, **args)
        parsed = urlparse(req.get_full_url())
        raw_str = parsed.path
        if parsed.query:
            raw_str += '?%s' % (parsed.query)
        raw_str += '\n'
        if req.has_data():
            raw_str += req.get_data()
        req.add_header('Authorization', auth.auth_interface_str(raw_str))
        return send_and_decode(req)
    return authed