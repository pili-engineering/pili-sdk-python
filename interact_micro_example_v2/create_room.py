# -*- coding: utf-8 -*-

from pili import RoomClient, Mac

# 替换成自己 Qiniu 账号的 AccessKey
access_key = "..."

# 替换成自己 Qiniu 账号的 SecretKey
secret_key = "..."


mac = Mac(access_key, secret_key)

room = RoomClient(mac)

print room.create_room_v2('admin_user', 'roomname')

print room.room_token_v2('roomname', 'admin_user', 'admin', 3600)


