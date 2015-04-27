import pili.api as api
import pili.conf as conf 

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
        self.play = Play(stream_id)
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

    def get_segments(self, start_second, end_second):
        res = api.get_segments(self.__auth__, stream_id=self.__stream_id__, start_second=start_second, end_second=end_second)
        return res


class Play(object):
    """
    Play is used to get the urls for playing the stream
    """
    def __init__(self, stream_id):
        _, self.__hub__, self.__title__ = stream_id.split('.')
    def __base__(self, protocol, host, profile):
        url = "%s://%s/%s/%s" % (protocol, host, self.__hub__, self.__title__)
        if profile!="":
            url += "@%s" % profile
        return url
    def rtmp_live(self, profile=""):
        return self.__base__("rtmp", conf.RTMP_PLAY_HOST, profile)
    def hls_live(self, profile=""):
        return self.__base__("http", conf.HLS_PLAY_HOST, profile)
    def hls_playback(self, start_second, end_second, profile=""):
        url = self.__base__("http", conf.HLS_PLAY_HOST, profile)
        url += "?start=%d&end=%d" % (start_second, end_second)
        return url
