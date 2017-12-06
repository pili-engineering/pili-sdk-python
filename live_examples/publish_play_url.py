# -*- coding: utf-8 -*-

import pili
import time

access_key = ""
secret_key = ""

domain = ''

hub_name = ''

stream_title = ''

expire = 3600

mac = pili.Mac(access_key, secret_key)
client = pili.Client(mac)

hub = client.hub(hub_name)


stream = hub.get("")


print pili.rtmp_publish_url(domain, hub_name, stream_title, mac, expire)

print pili.rtmp_play_url(domain, hub_name, stream_title)

print pili.hls_play_url(domain, hub_name, stream_title)

print pili.hdl_play_url(domain, hub_name, stream_title)

print pili.snapshot_play_url(domain, hub_name, stream_title)
