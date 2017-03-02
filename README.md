# Pili Streaming Cloud server-side library for Python

## Features

- URL
    - [x] RTMP推流地址: rtmp_publish_url(domain, hub, key, mac, expire_after_seconds)
    - [x] RTMP直播地址: rtmp_play_url(domain, hub, key)
    - [x] HLS直播地址: hls_play_url(domain, hub, key)
    - [x] HDL直播地址: hdl_play_url(domain, hub, key)
    - [x] 直播封面地址: snapshot_play_url(domain, hub, key)
- Hub
    - [x] 创建流: hub.create(key)
    - [x] 获得流: hub.get(key)
    - [x] 列出流: hub.list(prefix, limit, marker, liveonly)
    - [x] 批量查询直播状态: hub.batch_live_status(streams)

- Stream
    - [x] 流信息: stream.refresh()
    - [x] 禁用流: stream.disable(till)
    - [x] 启用流: stream.enable()
    - [x] 查询直播状态: stream.status()
    - [x] 保存直播回放: stream.saveas(start, end, options)
    - [x] 保存直播截图: stream.snapshot(options)
    - [x] 更改流的实时转码规格: stream.update_converts(profiles)
    - [x] 查询直播历史: stream.history(start, end)


## Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Configuration](#configuration)
    - [URL](#url)
        - [Generate RTMP publish URL](#generate-rtmp-publish-url)
        - [Generate RTMP play URL](#generate-rtmp-play-url)
        - [Generate HLS play URL](#generate-hls-play-url)
        - [Generate HDL play URL](#generate-hdl-play-url)
        - [Generate Snapshot play URL](#generate-snapshot-play-url)
    - [Hub](#hub)
        - [Instantiate a Pili Hub object](#instantiate-a-pili-hub-object)
        - [Create a new Stream](#create-a-new-stream)
        - [Get a Stream](#get-a-stream)
        - [List Streams](#list-streams)
        - [List live Streams](#list-live-streams)
        - [Batch query live status](#batch-query-live-status)
    - [Stream](#stream)
        - [Get Stream info](#get-stream-info)
        - [Disable a Stream](#disable-a-stream)
        - [Enable a Stream](#enable-a-stream)
        - [Get Stream live status](#get-stream-live-status)
        - [Save Stream live playback](#save-stream-live-playback)
        - [Save Stream snapshot](#save-stream-snapshot)
        - [Update Stream converts](#update-stream-converts)
        - [Get Stream history activity](#get-stream-history-activity)

## Installation

before next step, install git.

```
# install latest version
$ pip install pili2
```

## Usage

### Configuration

```python
import pili


access_key = "<QINIU ACCESS KEY>" # 替换成自己 Qiniu 账号的 AccessKey
secret_key = "<QINIU SECRET KEY>" # 替换成自己 Qiniu 账号的 SecretKey
hub_name = "<PILI HUB NAME>" # Hub 必须事先存在

mac = pili.Mac(AccessKey, SecretKey)
client = pili.Client(mac)
# ...
```

### URL

#### Generate RTMP publish URL

```python
print "RTMP publish URL:"
print pili.rtmp_publish_url("publish-rtmp.test.com", hub_name, "streamtitle", mac, 60)
# rtmp://publish-rtmp.test.com/PiliSDKTest/streamtitle?e=1488366903&token=Ge_kRfuV_4JW0hOCOnRq5_kD1sX53bKVht8FNdd3:TVrLvhQtDRmww5u1FV5AdwUDRD0=
```

#### Generate RTMP play URL

```python
print "RTMP play URL:"
print pili.rtmp_play_url("live-rtmp.test.com", hub_name, "streamtitle")
# rtmp://live-rtmp.test.com/PiliSDKTest/streamtitle
```

#### Generate HLS play URL

```python
print "HLS live URL:"
print pili.hls_play_url("live-hls.test.com", hub_name, "streamtitle")
# http://live-hls.test.com/PiliSDKTest/streamtitle.m3u8
```

#### Generate HDL play URL

```python
print "HDL live URL:"
print pili.hdl_play_url("live-hdl.test.com", hub_name, "streamtitle")
# http://live-hdl.test.com/PiliSDKTest/streamtitle.flv
```

#### Generate Snapshot play URL

```python
print "snapshot URL:"
print pili.snapshot_play_url("live-snapshot.test.com", hub_name, "streamtitle")
# http://live-snapshot.test.com/PiliSDKTest/streamtitle.jpg
```

### Hub

#### Instantiate a Pili Hub object

```python
mac = pili.Mac(AccessKey, SecretKey)
client = pili.Client(mac)
hub = client.hub("PiliSDKTest")
```

#### Create a new Stream

```python
stream = hub.create(stream_title1)
print "create stream:"
print stream
# {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream29479963631_1"}
```

#### Get a Stream

```python
print "get stream:"
stream = hub.get(stream_title1)
print stream
# {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream29479963631_1"}
```

#### List Streams

```python
print "list streams:"
print hub.list(prefix=stream_pre, limit=2)
# {u'marker': u'2', u'items': [{u'key': u'stream23057608792_3'}, {u'key': u'stream23057608792_2'}]}
```

#### List live Streams

```python
print "list live streams:"
print hub.list(liveonly=True)
# {u'marker': u'', u'items': [{u'key': u'test1'}]}
```

#### Batch query live status
```python
print "batch query live streams:",
print hub.batch_live_status(["test1", "test2"])
# [{u'key': u'test1', u'clientIP': u'172.21.2.14:63672', u'startAt': 1488377320, u'bps': 662200, u'fps': {u'data': 0, u'audio': 47, u'video': 25}}]
```

### Stream

#### Get Stream info

```python
print "get stream info:"
stream = hub.get(stream_title1)
print stream.refresh()
# {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream23057608792_1"}
```

#### Disable a Stream

```python
stream = hub.get(stream_title1)
print "before disable:", stream, stream.disabled()
stream.disable(int(time.time()) + 5)
print "after call disable:", stream.refresh(), stream.disabled()
time.sleep(5)
print "after sleep 5 seconds:", stream.refresh(), stream.disabled()

# before disable: {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream23126041129_1"} False
# after call disable: {"disabledTill": 1488378022, "converts": [], "hub": "PiliSDKTest", "key": "stream23126041129_1"} True
# after sleep 5 seconds: {"disabledTill": 1488378022, "converts": [], "hub": "PiliSDKTest", "key": "stream23126041129_1"} False
```

#### Enable a Stream

```python
stream.disable()
stream = hub.get(stream_title1)
stream.disable()
print "before enable:", stream.refresh(), stream.disabled()
stream.enable()
print "after enable:", stream.refresh(), stream.disabled()
# before enable: {"disabledTill": -1, "converts": [], "hub": "PiliSDKTest", "key": "stream23126041129_1"} True
# after enable: {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream23126041129_1"} False
```

#### Get Stream live status

```python
stream = hub.get("test1")
print "query stream live status:"
print stream.status()
# {u'clientIP': u'172.21.2.14:60209', u'startAt': 1488359924, u'bps': 672712, u'fps': {u'data': 0, u'audio': 47, u'video': 25}}
```

#### Save Stream live playback

```python
now = int(time.time())
print "save stream playback:"
print stream.saveas(start_second=now-300, fname="test1.m3u8")
# {u'fname': u'test1.m3u8'}
```

#### Save Stream snapshot
```python
print "save stream snapshot:"
print stream.snapshot(fname="test1.jpg")
# {u'fname': u'test1.jpg'}
```

#### Update Stream Converts
```python
stream = hub.get(stream_title1)
print "before update converts:", stream.refresh()
stream.update_converts(["480p", "720p"])

print "after update converts:", stream.refresh()
# before update converts: {"disabledTill": 0, "converts": [], "hub": "PiliSDKTest", "key": "stream24038673998_1"}
# after update converts: {"disabledTill": 0, "converts": ["480p", "720p"], "hub": "PiliSDKTest", "key": "stream24038673998_1"}
```


#### Get Stream history activity

```python
now = int(time.time())
print "get publish history:"
print stream.history(start_second=now-86400)
# [{u'start': 1488359927, u'end': 1488367483}, {u'start': 1488348110, u'end': 1488358759}, {u'start': 1488338678, u'end': 1488340383}, {u'start': 1488333270, u'end': 1488337953}, {u'start': 1488282646, u'end': 1488288321}]
```
