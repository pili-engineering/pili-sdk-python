import pili.api as api

class Stream(object):
    """
    Stream is used to control a stream. You should always create a Stream object by the
    interfaces of an application.
    """
    def __init__(self, auth, stream_id=None, data=None):
        if not (auth and (stream_id or data)):
            raise ValueError('invalid key')
        self.__auth__ = auth
        if not stream_id:
            stream_id = data["id"]
        self.__stream_id__ = stream_id
        self.__data__ = data

    def __getattr__(self, attr):
        if not self.__data__:
            self.refresh()
        return self.__data__[attr]

    def refresh(self):
        self.__data__ = api.get_stream(self.__auth__, stream_id=self.__stream_id__)
        return self.__data__

    def update(self, **args):
        res = api.update_stream(self.__auth__, stream_id=self.__stream_id__, **args)
        self.__data__ = res
        return res

    def delete(self):
        res = api.delete_stream(self.__auth__, stream_id=self.__stream_id__)
        return res

    def status(self):
        res = api.get_stream_status(self.__auth__, stream_id=self.__stream_id__)
        return res

