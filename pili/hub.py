import pili.api as api
from .stream import Stream
from .auth import Auth

class Hub():
    def __init__(self, access_key, secret_key, hub_name):
        if not (access_key and secret_key and hub_name):
            raise ValueError('invalid key')
        self.__auth__ = Auth(access_key, secret_key)
        self.__hub__ = hub_name

    def create_stream(self, **args):
        res = api.create_stream(self.__auth__, hub=self.__hub__, **args)
        return Stream(self.__auth__, data=res)

    def get_stream(self, stream_id):
        return Stream(self.__auth__, stream_id=stream_id)

    def streams(self, limit=None):
        marker = None
        while True:
            res = api.get_stream_list(self.__auth__, hub=self.__hub__, marker=marker, limit=None)
            if res["items"] != None:
                for data in res["items"]:
                    yield Stream(self.__auth__, data=data)
            else:
                break
            marker = res["marker"]


