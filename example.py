# -*- coding: utf-8 -*-

import os
import random
import sys
import time

import pili


def env(key):
    if key in os.environ:
        return os.environ[key]
    else:
        return ""


if __name__ == "__main__":
    if env("PILI_API_HOST") != "":
        pili.conf.API_HOST = env("PILI_API_HOST")

    access_key = env("QINIU_ACCESS_KEY")
    secret_key = env("QINIU_SECRET_KEY")
    if access_key == "" or secret_key == "":
        print "need set access_key and secret_key"
        sys.exit(1)

    mac = pili.Mac(access_key, secret_key)

    hub_name = "PiliSDKTest"

    client = pili.Client(mac)
    hub = client.hub(hub_name)

    stream_pre = "stream2" + str(int(random.random()*1e10))
    stream_title1 = stream_pre + "_1"
    stream_title2 = stream_pre + "_2"
    stream_title3 = stream_pre + "_3"

    stream = hub.create(stream_title1)
    print "create stream:"
    print stream

    print "get stream:"
    stream = hub.get(stream_title1)
    print stream

    print "get stream info:"
    stream = hub.get(stream_title1)
    print stream.refresh()

    stream = hub.create(stream_title2)
    print "create another stream:"
    print stream

    hub.create(stream_title3)

    print "list streams:"
    print hub.list(prefix=stream_pre, limit=2)

    print "list live streams:"
    print hub.list(liveonly=True)

    print "batch query live streams:"
    print hub.batch_live_status(["test1", "test2"])

    stream = hub.get(stream_title1)
    print "before disable:", stream, stream.disabled()
    stream.disable(int(time.time()) + 5)
    print "after call disable:", stream.refresh(), stream.disabled()
    time.sleep(5)
    print "after sleep 5 seconds:", stream.refresh(), stream.disabled()

    stream = hub.get(stream_title1)
    stream.disable()
    print "before enable:", stream.refresh(), stream.disabled()
    stream.enable()
    print "after enable:", stream.refresh(), stream.disabled()

    stream = hub.get(stream_title1)
    print "before update converts:", stream.refresh()
    stream.update_converts(["480p", "720p"])
    print "after update converts:", stream.refresh()

    stream = hub.get("test1")
    print "query stream live status:"
    print stream.status()

    now = int(time.time())
    print "save stream playback:"
    print stream.saveas(start_second=now-300, fname="test1.m3u8")

    print "save stream snapshot:"
    print stream.snapshot(fname="test1.jpg")

    now = int(time.time())
    print "get publish history:"
    print stream.history(start_second=now-86400)

    print "RTMP publish URL:"
    print pili.rtmp_publish_url("publish-rtmp.test.com", hub_name, "streamtitle", mac, 60)

    print "RTMP play URL:"
    print pili.rtmp_play_url("live-rtmp.test.com", hub_name, "streamtitle")

    print "HLS live URL:"
    print pili.hls_play_url("live-hls.test.com", hub_name, "streamtitle")

    print "HDL live URL:"
    print pili.hdl_play_url("live-hdl.test.com", hub_name, "streamtitle")

    print "snapshot URL:"
    print pili.snapshot_play_url("live-snapshot.test.com", hub_name, "streamtitle")
