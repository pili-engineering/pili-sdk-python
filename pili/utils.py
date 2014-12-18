from urllib2 import urlopen
import contextlib
import json

def send_and_decode(req):
    with contextlib.closing(urlopen(req)) as f:
        raw = f.read()
        return json.loads(raw)