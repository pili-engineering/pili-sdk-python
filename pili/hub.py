# -*- coding: utf-8 -*-

import pili.api as api
from .stream import Stream


class Hub(object):
    def __init__(self, mac, hub):
        self.__auth__ = mac.__auth__
        self.__hub__ = hub

    # create 创建一路流
    def create(self, key):
        api.create_stream(self.__auth__, hub=self.__hub__, key=key)
        return Stream(self.__auth__, hub=self.__hub__, key=key)

    # 获取一路流
    def get(self, key):
        return Stream(self.__auth__, hub=self.__hub__, key=key)

    """
    list 遍历hub的流列表
    输入参数:
        prefix: 字符串，匹配的流名前缀
        liveonly: 布尔值，可选，如果为True则只列出正在直播的流
        limit: 正整数，限定了一次最多可以返回的流个数，实际返回的流个数可能会小于这个值
        marker: 字符串，上一次遍历得到的游标
    返回值:
        items: 字符串数组，查询返回的流名
        marker: 这次遍历得到的游标，下次请求应该带上，如果为""，则表示已遍历完所有流
    """
    def list(self, **kwargs):
        res = api.get_stream_list(self.__auth__, hub=self.__hub__, **kwargs)
        return res

    """
    batch_live_status 批量查询流的直播信息
    输入参数:
        streams: 要查询的流名数组，长度不能超过100
    返回值: 如下结构体的数组
        key: 流名
        startAt: 直播开始的Unix时间戳
        clientIP: 推流的客户端IP
        bps: 正整数 码率
        fps:
            audio: 正整数，音频帧率
            video: 正整数，视频帧率
            data: 正整数，数据帧率
    """
    def batch_live_status(self, streams):
        res = api.batch_live_status(self.__auth__, hub=self.__hub__, streams=streams)
        return res["items"]

    def bandwidth_count_now(self):
        res = api.bandwidth_count_now(self.__auth__, hub=self.__hub__)
        return res

    def bandwidth_count_history(self, start, end, limit=None, marker=None):
        res = api.bandwidth_count_history(self.__auth__, hub=self.__hub__, start=start, end=end, limit=limit,
                                          marker=marker)
        return res

    def bandwidth_count_detail(self, time):
        res = api.bandwidth_count_detail(self.__auth__, hub=self.__hub__, time=time)
        return res
