# PILI直播 Python服务端SDK 使用指南

## 功能列表

- 直播流的创建、获取和列举
    - [x] hub.createStream()  // 创建流
    - [x] hub.getStream()  // 获取流
    - [x] hub.listStreams()  // 列举流
- 直播流的其他功能
    - [x] stream.toJsonString()  // 流信息转为json
    - [x] stream.update()      // 更新流
    - [x] stream.disable()      // 禁用流
    - [x] stream.enable()    // 启用流
    - [x] stream.rtmpPublishUrl()   // 生成推流地址
    - [x] stream.rtmpLiveUrls()    // 生成rtmp播放地址
    - [x] stream.hlsLiveUrls()   // 生成hls播放地址
    - [x] stream.httpFlvLiveUrls()   // 生成flv播放地址
    - [x] stream.status()     // 获取流状态
    - [x] stream.segments()      // 获取流片段
    - [x] stream.hlsPlaybackUrls()  // 生成hls回看地址
    - [x] stream.saveAs()        // 流另存为文件
    - [x] stream.snapshot()      // 获取快照
    - [x] stream.delete()    // 删除流


## 目录

- [安装](#installation)
- [用法](#usage)
    - [配置](#configuration)
    - [Hub](#hub)
        - [实例化hub对象](#instantiate-a-pili-hub-object)
        - [创建流](#create-a-new-stream)
        - [获取流](#get-an-exist-stream)
        - [列举流](#list-streams)
    - [直播流](#stream)
        - [流信息转为json](#to-json-string)
        - [更新流](#update-a-stream)
        - [禁用流](#disable-a-stream)
        - [启用流](#enable-a-stream)
        - [生成推流地址](#generate-rtmp-publish-url)
        - [生成rtmp播放地址](#generate-rtmp-live-play-urls)
        - [生成hls播放地址](#generate-hls-play-urls)
        - [生成flv播放地址](#generate-http-flv-live-play-urls)
        - [获取流状态](#get-stream-status)
        - [获取流片段](#get-stream-segments)
        - [生成hls回看地址](#generate-hls-playback-urls)
        - [流另存为文件](#save-stream-as-a-file)
        - [获取快照](#snapshot-stream)
        - [删除流](#delete-a-stream)
- [History](#history)


<a id="installation"></a>
## 安装

```shell
pip install pili
# 提示: 1.2版本以后的接口有变化
#       若需要使用旧版API, 使用 pip install -v pili==0.1.0.
```

<a id="usage"></a>
## 用法:

<a id="configuration"></a>
#### 配置

```python
from pili import *

access_key = 'qiniu_access_key' 
secret_key = 'qiniu_secret_key'

hub_name   = 'pili_hub_name' # The Hub must be exists before use

# 如有需要可以更改API host
# 
# 默认为 pili.qiniuapi.com
# pili-lte.qiniuapi.com 为最近更新版本
# 
# conf.API_HOST = 'pili.qiniuapi.com' # 默认
```

### Hub

<a id="instantiate-a-pili-hub-object"></a>
#### 实例化hub对象

```python
credentials = Credentials(access_key, secret_key)
hub = Hub(credentials, hub_name)
```

<a id="create-a-new-stream"></a>
#### 创建流

```python
# title          : 可选，默认自动生成
# publishKey     : 可选，默认自动生成
# publishSecrity : 可选, 可以为 "dynamic" 或 "static", 默认为 "dynamic"
stream = hub.create_stream(title=None, publishKey=None, publishSecurity="static")
# return stream object...
print "\ncreate_stream()\n", stream.to_json()
# {
#   "publishSecurity": "dynamic",
#   "hub": "test-origin",
#   "title": "55db4a9ee3ba573b20000004",
#   "publishKey": "976655fbf3bee71e",
#   "disabled": false,
#   "hosts": {
#     "live": {
#       "http": "e4kvkh.live1-http.z1.pili.qiniucdn.com",
#       "rtmp": "e4kvkh.live1-rtmp.z1.pili.qiniucdn.com"
#     },
#     "playback": {
#       "http": "e4kvkh.playback1.z1.pili.qiniucdn.com"
#     },
#     "publish": {
#       "rtmp": "e4kvkh.publish.z1.pili.qiniup.com"
#     }
#   },
#   "updatedAt": "2015-08-24T16:47:26.786Z",
#   "id": "z1.test-origin.55db4a9ee3ba573b20000004",
#   "createdAt": "2015-08-24T16:47:26.786Z"
# }
```

<a id="get-an-exist-stream"></a>
#### 获取流

```python
# stream_id: 必填，String 类型
stream = hub.get_stream(stream_id=id)
# 返回直播流对象
print "\nget_stream()\n", stream
# <pili.stream.Stream object at 0x106365490>
```

<a id="list-streams"></a>
#### 列举流

```python
# marker : 选填，String 类型
# limit  : 选填, int 类型
# title  : 选填, string 类型
res = hub.list_streams(marker=None, limit=10, title="prefix_")
for s in res["items"]:
    # s is stream object...
    # Do someting...
    pass
next = hub.list_streams(marker=res["marker"])
print "\nlist_streams()\n", res
# {
#   "marker": "10",
#   "items": [
#     <pili.stream.Stream object at 0x106365490>,
#     <pili.stream.Stream object at 0x1063654d0>,
#     <pili.stream.Stream object at 0x106365510>,
#     <pili.stream.Stream object at 0x106365550>,
#     <pili.stream.Stream object at 0x106365590>,
#     <pili.stream.Stream object at 0x1063655d0>,
#     <pili.stream.Stream object at 0x106365610>,
#     <pili.stream.Stream object at 0x106365650>,
#     <pili.stream.Stream object at 0x106365690>,
#     <pili.stream.Stream object at 0x1063656d0>
#   ]
# }
```

<a id="stream"></a>
### 直播流
<a id="to-json-string"></a>
#### 流信息转为json

```python
print stream.to_json()
# {
#   "publishSecurity":"static",
#   "hub":"test-origin",
#   "title":"55db4ecae3ba573b20000006",
#   "publishKey":"new_secret_words",
#   "disabled":false,
#   "hosts":{
#     "live":{
#       "http":"e4kvkh.live1-http.z1.pili.qiniucdn.com",
#       "rtmp":"e4kvkh.live1-rtmp.z1.pili.qiniucdn.com"
#     },
#     "playback":{
#       "http":"e4kvkh.playback1.z1.pili.qiniucdn.com"
#     },
#     "publish":{
#       "rtmp":"e4kvkh.publish.z1.pili.qiniup.com"
#     }
#   },
#   "updatedAt":"2015-08-24T13:05:15.272975102-04:00",
#   "id":"z1.test-origin.55db4ecae3ba573b20000006",
#   "createdAt":"2015-08-24T13:05:14.526-04:00"
# }
```

<a id="update-a-stream"></a>
#### 更新流

```python
# publishKey     : optional, string
# publishSecrity : optional, string
# disabled       : optional, bool
stream.update(publishKey = "new_secret_words", publishSecurity="dynamic")
```

<a id="disable-a-stream"></a>
#### 禁用流

```python
stream.disable()
```

<a id="enable-a-stream"></a>
#### 启用流

```python
stream.enable()
```

<a id="generate-rtmp-publish-url"></a>
#### 生成推流地址

```python
url = stream.rtmp_publish_url()
print url
# rtmp://e4kvkh.publish.z1.pili.qiniup.com/test-origin/55db52e1e3ba573b2000000e?key=new_secret_words
```

<a id="generate-rtmp-live-play-urls"></a>
#### 生成rtmp播放地址

```python
urls = stream.rtmp_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original RTMP live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "rtmp://e4kvkh.live1-rtmp.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e"}
```

<a id="generate-hls-play-urls"></a>
#### 生成hls播放地址

```python
urls = stream.hls_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original HLS live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.m3u8"}
```

<a id="generate-http-flv-live-play-urls"></a>
#### 生成flv播放地址

```python
urls = stream.http_flv_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original Http-Flv live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.flv"}
```

<a id="get-stream-status"></a>
#### 获取流状态

```python
status = stream.status()
print status
# {
#     "addr": "222.73.202.226:2572",
#     "status": "connected",
#     "bytesPerSecond": 16870.200000000001,
#     "framesPerSecond": { 
#         "audio": 42.200000000000003,
#         "video": 14.733333333333333,
#         "data": 0.066666666666666666,
#     }
# }
```

<a id="get-stream-segments"></a>
#### 获取流片段

```python
# start_second : 选填, int64, 单位为秒, 为UNIX时间戳
# end_second   : 选填, int64, 单位为秒, 为UNIX时间戳
# limit        : 选填, uint32
# ...注意：如上时间参数，要么都传参，要么都传None
segments = stream.segments(start_second=None, end_second=None, limit=None)
print segments
# [
#     {
#         "start": 1440282134,
#         "end": 1440437833
#     },
#     {
#         "start": 1440437981,
#         "end": 1440438835
#     },
#     ...
# ]
```

<a id="generate-hls-playback-urls"></a>
#### 生成hls回看地址

```python
# start : 必填, int64, 单位为秒, 为UNIX时间戳
# end   : 必填, int64, 单位为秒, 为UNIX时间戳
urls = stream.hls_playback_urls(start, end)
for k in urls:
    print k, ":", urls[k]

# Get original HLS playback url
original_url = urls["ORIGIN"]
```

<a id="save-stream-as-a-file"></a>
#### 流另存为文件

```python
# name      : 必填, string 类型
# format    : 必填, string 类型 更多请参考 http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# start     : 选填, int64, 单位为秒, 为UNIX时间戳
# end       : 选填, int64, 单位为秒, 为UNIX时间戳
# notifyUrl : 选填, string 类型
res = stream.save_as(name="videoName.mp4", format="mp4", start=1440282134, end=1440437833, notifyUrl=None)
print res
# {
#     "url": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.m3u8",
#     "targetUrl": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.mp4",
#     "persistentId": "z1.55d81c6c7823de5a49ad77b3"
# }
```

<a id="snapshot-stream"></a>
#### 获取快照

```python
# name      : 必填, string 类型
# format    : 必填, string 类型 更多请参考 http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# time      : 选填, int64, 单位为秒, 为UNIX时间戳
# notifyUrl : 选填, string 类型
res = stream.snapshot(name="imageName.jpg", format="jpg", time=None, notifyUrl=None)
print res
# {
#     "targetUrl": "http://ey636h.static1.z1.pili.qiniucdn.com/snapshots/z1.test-hub.55d81a72e3ba5723280000ec/imageName.jpg",
#     "persistentId": "z1.55d81c247823de5a49ad729c"
# }
```

当使用 `saveAs()` 和 `snapshot()` 的时候, 由于是异步处理， 你可以在七牛的FOP接口上使用 `persistentId`来获取处理进度.参考如下：   
API: `curl -D GET http://api.qiniu.com/status/get/prefop?id={persistentId}`  
文档说明: <http://developer.qiniu.com/docs/v6/api/overview/fop/persistent-fop.html#pfop-status>  

<a id="delete-a-stream"></a>
#### 删除流

```python
stream.delete()
```

## History

- 1.5.0
    - Update Stream Create,Get,List
        - hub.create_stream()
        - hub.get_stream()
        - hub.list_streams()
    - Add Stream operations else
        - stream.to_json()
        - stream.update()
        - stream.disable()
        - stream.enable()
        - stream.rtmp_publish_url()
        - stream.rtmp_live_urls()
        - stream.hls_live_urls()
        - stream.http_flv_live_urls()
        - stream.status()
        - stream.segments()
        - stream.hls_playback_urls()
        - stream.snapshot()
        - stream.save_as()
        - stream.delete()
