import pili.api as api
import pili.conf as conf 
import time
from .utils import __hmac_sha1__
from urlparse import urlparse

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
        self.play = Play(stream_id)
        self.publish= Publish(stream_id, self.publishSecurity, self.publishKey)

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
        self.rtmp_play_host = conf.RTMP_PLAY_HOST
        self.hls_play_host = conf.HLS_PLAY_HOST
    def __base__(self, protocol, host, profile):
        url = "%s://%s/%s/%s" % (protocol, host, self.__hub__, self.__title__)
        if profile!="":
            url += "@%s" % profile
        return url
    def rtmp_live(self, profile=""):
        return self.__base__("rtmp", self.rtmp_play_host, profile)
    def hls_live(self, profile=""):
        return self.__base__("http", self.hls_play_host, profile)
    def hls_playback(self, start_second, end_second, profile=""):
        url = self.__base__("http", self.hls_play_host, profile)
        url += "?start=%d&end=%d" % (start_second, end_second)
        return url

class Publish(object):
    """
    Publish is used to get the urls for publishing the stream
    """
    def __init__(self, stream_id, security, key):
        _, self.__hub__, self.__title__ = stream_id.split('.')
        self.__security__ = security
        self.__key__ = str(key)
        self.rtmp_publish_host = conf.RTMP_PUBLISH_HOST
    def __base__(self, protocol, host, profile):
        return url
    def url(self, nonce=None):
        url = "rtmp://%s/%s/%s" % (self.rtmp_publish_host, self.__hub__, self.__title__)
        if self.__security__ == "static":
            url += "?key=%s" % self.__key__
        elif self.__security__ == "dynamic":
            if nonce == None:
                nonce = str(int(time.time()*1000))
            url += "?nonce=%s" % nonce
            parsed = urlparse(url)
            data = "%s?%s" % (parsed.path, parsed.query)
            token = __hmac_sha1__(data, self.__key__)
            url += "&token=%s" % token
            pass
        else:
            return None
        return url
