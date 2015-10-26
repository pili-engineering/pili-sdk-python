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
    def __init__(self, auth, stream_id=None, data=None):
        self.__auth__ = auth
        if not (stream_id or data):
            raise ValueError('invalid key')
        if not stream_id:
            stream_id = data["id"]
        self.__stream_id__ = stream_id
        self.__data__ = data

    def __getattr__(self, attr):
        if not self.__data__:
            self.refresh()
        try:
            return self.__data__ if attr == "data" else self.__data__[attr]
        except:
            return None

    def refresh(self):
        self.__data__ = api.get_stream(self.__auth__, stream_id=self.__stream_id__)
        return self

    def update(self, **args):
        res = api.update_stream(self.__auth__, stream_id=self.__stream_id__, **args)
        self.__data__ = res
        return self

    def disable(self):
        return self.update(disabled=True)

    def enable(self):
        return self.update(disabled=False)

    def status(self):
        res = api.get_status(self.__auth__, stream_id=self.__stream_id__)
        return res

    def segments(self, start_second=None, end_second=None, limit=None):
        res = api.get_segments(self.__auth__, stream_id=self.__stream_id__, start_second=start_second, end_second=end_second, limit=limit)
        return res

    def save_as(self, **args):
        res = api.save_stream_as(self.__auth__, stream_id=self.__stream_id__, **args)
        return res

    def snapshot(self, **args):
        res = api.snapshot_stream(self.__auth__, stream_id=self.__stream_id__, **args)
        return res

    def delete(self):
        res = api.delete_stream(self.__auth__, stream_id=self.__stream_id__)
        return res

    def __base__(self, protocol, host, profile):
        url = "%s://%s/%s/%s" % (protocol, host, self.hub, self.title)
        if profile!="":
            url += "@%s" % profile
        return url

    def rtmp_live_urls(self):
        res = dict()
        res["ORIGIN"] = self.__base__("rtmp", self.hosts["live"]["rtmp"], "")
        if self.profiles!=None:
            for profile in self.profiles:
                res[profile] = self.__base__("rtmp", self.hosts["live"]["rtmp"], profile)
        return res

    def http_flv_live_urls(self):
        res = dict()
        res["ORIGIN"] = self.__base__("http", self.hosts["live"]["hdl"], "") + ".flv"
        if self.profiles!=None:
            for profile in self.profiles:
                res[profile] = self.__base__("http", self.hosts["live"]["hdl"], profile) + ".flv"
        return res

    def hls_live_urls(self):
        res = dict()
        res["ORIGIN"] = self.__base__("http", self.hosts["live"]["hls"], "") + ".m3u8"
        if self.profiles!=None:
            for profile in self.profiles:
                res[profile] = self.__base__("http", self.hosts["live"]["hls"], profile) + ".m3u8"
        return res

    def hls_playback_urls(self, start_second, end_second):
        res = dict()
        url = self.__base__("http", self.hosts["playback"]["hls"], "") + ".m3u8"
        url += "?start=%d&end=%d" % (start_second, end_second)
        res["ORIGIN"] = url
        if self.profiles!=None:
            for profile in self.profiles:
                url = self.__base__("http", self.hosts["playback"]["hls"], profile) + ".m3u8"
                url += "?start=%d&end=%d" % (start_second, end_second)
                res[profile] = url
        return res

    def rtmp_publish_url(self):
        url = "rtmp://%s/%s/%s" % (self.hosts["publish"]["rtmp"], self.hub, self.title)
        if self.publishSecurity == "static":
            url += "?key=%s" % self.publishKey
        elif self.publishSecurity == "dynamic":
            nonce = str(int(time.time()))
            url += "?nonce=%s" % nonce
            data = "/%s/%s?nonce=%s" % (self.hub, self.title, nonce)
            token = __hmac_sha1__(data, str(self.publishKey))
            url += "&token=%s" % token
        else:
            return None
        return url

    def to_json(self):
        return json.dumps(self.data)
