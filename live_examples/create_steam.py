# -*- coding: utf-8 -*-

import pili

# 替换成自己 Qiniu 账号的 AccessKey
access_key = "..."

# 替换成自己 Qiniu 账号的 SecretKey
secret_key = "..."


hub_name = ''
stream_name = ''

mac = pili.Mac(access_key, secret_key)

client = pili.Client(mac)

hub = client.hub(hub_name)

hub.create(stream_name)
