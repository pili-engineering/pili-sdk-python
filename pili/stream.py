# -*- coding: utf-8 -*-

import json
import time

import pili.api as api


class Stream(object):
    """
    Stream属性
        hub: 字符串类型，hub名字
        key: 字符串类型，流名
        disabledTill: 整型，Unix时间戳，在这之前流均不可用，-1表示永久不可用
        converts: 字符串数组，流的转码规格
    """
    def __init__(self, auth, hub, key):
        self.__auth__ = auth
        if not (hub and key):
            raise ValueError('invalid key')
        self.key = key
        self.hub = hub
        self.__data__ = None

    def __getattr__(self, attr):
        if not self.__data__:
            self.refresh()
        try:
            return self.__data__ if attr == "data" else self.__data__[attr]
        except KeyError, e:
            return e.message

    def __repr__(self):
        return self.to_json()

    # refresh 主动更新流信息，会产生一次rpc调用
    def refresh(self):
        data = api.get_stream(self.__auth__, hub=self.hub, key=self.key)
        self.__data__ = {}
        for p in ["disabledTill", "converts"]:
            self.__data__[p] = data[p] if p in data else None
        self.__data__["key"] = self.key
        self.__data__["hub"] = self.hub
        return self

    # disable 禁用流，till Unix时间戳，在这之前流均不可用
    def disable(self, till=None):
        if till is None:
            till = -1
        return api.disable_stream(self.__auth__, hub=self.hub, key=self.key, till=till)

    # disabled 判断流是否被禁用
    def disabled(self):
        return self.disabledTill == -1 or self.disabledTill > int(time.time())

    # enable 开启流
    def enable(self):
        return api.disable_stream(self.__auth__, hub=self.hub, key=self.key, till=0)

    """
    status 查询直播信息
    返回值:
        startAt: 直播开始的Unix时间戳
        clientIP: 推流的客户端IP
        bps: 正整数 码率
        fps:
            audio: 正整数，音频帧率
            video: 正整数，视频帧率
            data: 正整数，数据帧率
    """
    def status(self):
        res = api.get_status(self.__auth__, hub=self.hub, key=self.key)
        return res

    """
    history 查询直播历史
    输入参数:
        start_second: Unix时间戳，起始时间，可选，默认不限制起始时间
        end_second: Unix时间戳，结束时间，可选，默认为当前时间
    返回值: 如下结构的数组
        start: Unix时间戳，直播开始时间
        end: Unix时间戳，直播结束时间
    """
    def history(self, start_second=None, end_second=None):
        res = api.get_history(self.__auth__, hub=self.hub, key=self.key, start=start_second, end=end_second)
        return res["items"]

    # save_as等同于saveas接口，出于兼容考虑，暂时保留
    def save_as(self, start_second=None, end_second=None, **kwargs):
        return self.saveas(start_second, end_second, **kwargs)

    """
    saveas 保存直播回放到存储空间
    输入参数:
        start_second: Unix时间戳，起始时间，可选，默认不限制起始时间
        end_second: Unix时间戳，结束时间，可选，默认为当前时间
        fname: 保存的文件名，可选，不指定会随机生产
        format: 保存的文件格式，可选，默认为m3u8，如果指定其他格式则保存动作为异步模式
        pipeline: dora的私有队列，可选，不指定则使用默认队列
        notify: 保存成功后的回调通知地址
        expireDays:  对应ts文件的过期时间
                    -1 表示不修改ts文件的expire属性
                    0  表示修改ts文件生命周期为永久保存
                    >0 表示修改ts文件的的生命周期为expireDay
    返回值:
        fname: 保存到存储空间的文件名
        persistentID: 异步模式时，持久化异步处理任务ID，通常用不到该字段
    """
    def saveas(self, start_second=None, end_second=None, **kwargs):
        kwargs["hub"] = self.hub
        kwargs["key"] = self.key
        if start_second is not None:
            kwargs["start"] = start_second
        if end_second is not None:
            kwargs["end"] = end_second
        res = api.stream_saveas(self.__auth__, **kwargs)
        return res

    """
    snapshot 保存直播截图到存储空间
    输入参数:
        time: Unix时间戳，要保存的时间点，默认为当前时间
        fname: 保存的文件名，可选，不指定会随机生产
        format: 保存的文件格式，可选，默认为jpg
    返回值:
        fname: 保存到存储空间的文件名
    """
    def snapshot(self, **kwargs):
        kwargs["hub"] = self.hub
        kwargs["key"] = self.key
        res = api.stream_snapshot(self.__auth__, **kwargs)
        return res

    """
    update_converts 更改流的转码规格
    输入参数:
        profiles: 字符串数组，实时转码规格
    返回值: 无
    """
    def update_converts(self, profiles=[]):
        res = api.update_stream_converts(self.__auth__, hub=self.hub, key=self.key, profiles=profiles)
        return res

    def to_json(self):
        return json.dumps(self.data)
