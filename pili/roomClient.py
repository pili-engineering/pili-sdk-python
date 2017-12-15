import hmac
import hashlib
import json
import time
import pili.api as api
from utils import urlsafe_base64_encode


class RoomClient(object):
    """docstring for RoomClient"""
    def __init__(self, credentials):
        self.__credentials__ = credentials
        self.__auth__ = credentials.__auth__

    def createRoom(self, ownerId, roomName=None, version='v1'):
        res = api.create_room(self.__auth__, ownerId=ownerId, roomName=roomName, version=version)
        return res

    def getRoom(self, roomName, version='v1'):
        res = api.get_room(self.__auth__, roomName=roomName, version=version)
        return res

    def deleteRoom(self, roomName, version='v1'):
        res = api.delete_room(self.__auth__, roomName=roomName, version=version)
        return res

    def getUser(self, roomName, version='v1'):
        res = api.get_user(self.__auth__, roomName=roomName, version=version)
        return res

    def deleteUser(self, roomName, userId, version='v1'):
        res = api.delete_user(self.__auth__, roomName=roomName, userId=userId, version=version)
        return res

    def roomToken(self, roomName, userId, perm, expireAt, version=None):
        if version == 'v2':
            params = {"version": "2.0", "room_name": roomName,
                      "user_id": userId, "perm": perm,
                      "expire_at": int(time.time()) + expireAt}
        else:
            params = {"room_name": roomName,
                      "user_id": userId, "perm": perm,
                      "expire_at": int(time.time()) + expireAt}

        roomAccessString = json.dumps(params, separators=(',', ':'))
        encodedRoomAccess = urlsafe_base64_encode(roomAccessString)
        hashed = hmac.new(self.__auth__.secret_key, encodedRoomAccess, hashlib.sha1)
        encodedSign = urlsafe_base64_encode(hashed.digest())
        return self.__auth__.access_key+":"+encodedSign+":"+encodedRoomAccess
