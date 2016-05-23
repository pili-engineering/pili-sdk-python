import pili.api as api
import pili.conf as conf
from .utils import __hmac_sha1__
import json
import time

class Stream(object):
    """
    Stream is used to control a stream. You should always create a Stream object by the
    interfaces of an application.
    """
    def __init__(self, auth, hub, key):
        self.__auth__ = auth
        if not (hub and key):
            raise ValueError('invalid key')
        self.key = key
        self.hub = hub
        self.__data__ = None

    def __getattr__(self, attr):
        if not self.__data__:
            self.refresh()
        try:
            return self.__data__ if attr == "data" else self.__data__[attr]
        except:
            return None

    def refresh(self):
        self.__data__ = api.get_stream(self.__auth__, hub=self.hub, key=self.key)
        self.__data__["key"] = self.key
        self.__data__["hub"] = self.hub
        return self

    def disable(self, till=None):
        if till == None:
            till = -1
        return api.disable_stream(self.__auth__, hub=self.hub, key=self.key, till=till)

    def enable(self):
        return api.disable_stream(self.__auth__, hub=self.hub, key=self.key, till=0)

    def status(self):
        res = api.get_status(self.__auth__, hub=self.hub, key=self.key)
        return res

    def history(self, start_second=None, end_second=None):
        res = api.get_history(self.__auth__, hub=self.hub, key=self.key, start=start_second, end=end_second)
        return res

    def save_as(self, start_second=None, end_second=None):
        res = api.save_stream_as(self.__auth__, hub=self.hub, key=self.key, start=start_second, end=end_second)
        return res

    def to_json(self):
        return json.dumps(self.data)
