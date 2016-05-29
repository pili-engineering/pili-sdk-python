import pili.api as api
from .stream import Stream

class Hub(object):
    def __init__(self, mac, hub):
        self.__auth__ = mac.__auth__
        self.__hub__ = hub

    def create(self, key):
        res = api.create_stream(self.__auth__, hub=self.__hub__, key=key)
        return Stream(self.__auth__, hub=self.__hub__, key=key)

    def get(self, key):
        return Stream(self.__auth__, hub=self.__hub__, key=key)

    def list(self, **args):
        res = api.get_stream_list(self.__auth__, hub=self.__hub__, **args)
        items = []
        for data in res["items"] if res["items"] is not None else []:
            items.append(Stream(self.__auth__, hub=self.__hub__, key=data["key"]))
        res["items"] = items
        return res
