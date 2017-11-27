# -*- coding: utf-8 -*-

import pili

access_key = ""
secret_key = ""


hub_name = ''

stream_name = ''

mac = pili.Mac(access_key, secret_key)
client = pili.Client(mac)
hub = client.hub(hub_name)
stream = hub.get(stream_name)

print(stream.history(start_second=123, end_second=321))
