"""
Utils
"""
from urllib2 import urlopen
import contextlib
import json

def send_and_decode(req):
    """
    Send the request and return the decoded json of response.

    Args:
        req: urllib2.Request

    Returns:
        A dict of decoded response
    """
    with contextlib.closing(urlopen(req)) as res:
        raw = res.read()
        return json.loads(raw)

