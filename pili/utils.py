"""
Utils
"""
from urllib2 import urlopen, HTTPError
import contextlib, json
from .errors import APIError

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
            raw = res.read()
            return json.loads(raw)
    except HTTPError, res:
        raw = res.read()
        try:
            data = json.loads(raw)
        except ValueError:
            raise APIError(res.code, res.reason)
        else:
            raise APIError(data["error"], data["message"])

