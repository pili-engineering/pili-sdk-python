# -*- coding: utf-8 -*-

import pili

access_key = ""
secret_key = ""

hub_name = ''
mac = pili.Mac(access_key, secret_key)
client = pili.Client(mac)

hub = client.hub(hub_name)


stream = hub.get("")
print(stream.update_converts(["480p", "720p"]))
