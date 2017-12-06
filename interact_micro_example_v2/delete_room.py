# -*- coding: utf-8 -*-

from pili import RoomClient, Mac

access_key = "..." # 替换成自己 Qiniu 账号的 AccessKey
secret_key = "..." # 替换成自己 Qiniu 账号的 SecretKey


mac = Mac(access_key, secret_key)

room = RoomClient(mac)

print room.delete_room_v2('roomname')



