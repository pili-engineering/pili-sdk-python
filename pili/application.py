import pili.api as api
from .stream import Stream
from .auth import Auth

class Application(object):
    """
    Application is equivalent to the application model in API, all streams is
    managed in here.
    """
    def __init__(self, access_key, secret_key):
        if not (access_key and secret_key):
            raise ValueError('invalid key')
        self.__auth__ = Auth(access_key, secret_key)

    def create_stream(self, **args):
        res = api.create_stream(self.__auth__, **args)
        return Stream(self.__auth__, data=res)

    def get_stream(self, stream_id):
        return Stream(self.__auth__, stream_id=stream_id)

    def get_stream_list(self):
        res = api.get_stream_list(self.__auth__)
        streams = []
        if res['total'] > 0:
            for data in res["streams"]:
                streams.append(Stream(self.__auth__, data=data))
        return streams

