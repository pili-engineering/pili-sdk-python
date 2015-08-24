import pili.api as api
from .stream import Stream

class Hub(object):
    def __init__(self, credentials, hub_name):
        self.__auth__ = credentials.__auth__
        self.__hub__ = hub_name

    def create_stream(self, **args):
        res = api.create_stream(self.__auth__, hub=self.__hub__, **args)
        return Stream(self.__auth__, data=res)

    def get_stream(self, stream_id):
        return Stream(self.__auth__, stream_id=stream_id)

    def list_streams(self, marker=None, limit=None):
        res = api.get_stream_list(self.__auth__, hub=self.__hub__, marker=marker, limit=limit)
        items = []
        for data in res["items"]:
            items.append(Stream(self.__auth__, stream_id=data["id"]))
        res["items"] = items
        return res