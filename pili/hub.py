import pili.api as api
from .stream import Stream

def create_stream(hub, **args):
    res = api.create_stream(hub=hub, **args)
    return Stream(data=res)

def get_stream(stream_id):
    return Stream(stream_id=stream_id)

def streams(hub, limit=None):
    marker = None
    while True:
        res = api.get_stream_list(hub=hub, marker=marker, limit=None)
        if res["items"] is not None:
            for data in res["items"]:
                yield Stream(data=data)
        else:
            break
        marker = res["marker"]