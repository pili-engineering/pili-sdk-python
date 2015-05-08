"""
Utils
"""
from urllib2 import urlopen, HTTPError
import contextlib, json
from .errors import APIError
import hmac, hashlib, base64

def send_and_decode(req):
    """
    Send the request and return the decoded json of response.

    Args:
        req: urllib2.Request

    Returns:
        A dict of decoded response
    """
    try:
        with contextlib.closing(urlopen(req)) as res:
            if res.getcode() == 204:
                return None
            raw = res.read()
            return json.loads(raw)
    except HTTPError, res:
        raw = res.read()
        try:
            data = json.loads(raw)
        except ValueError:
            raise APIError(res.reason)
        else:
            raise APIError(data["error"])

def __hmac_sha1__(data, key):
    """
    hmac-sha1
    """
    hashed = hmac.new(key, data, hashlib.sha1)
    return base64.urlsafe_b64encode(hashed.digest())
