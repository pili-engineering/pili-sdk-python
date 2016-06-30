# Pili Streaming Cloud server-side library for Python

## Features

- URL
    - [x] RTMP推流地址: rtmp_publish_url(domain, hub, key, mac, expire_after_seconds)
    - [x] RTMP直播地址: rtmp_play_url(domain, hub, key)
    - [x] HLS直播地址: hls_play_url(domain, hub, key)
    - [x] HDL直播地址: hdl_play_url(domain, hub, key)
    - [x] 截图直播地址: snapshot_play_url(domain, hub, key)
- Hub
    - [x] 创建流: hub.create(key)
    - [x] 获得流: hub.get(key)
    - [x] 列出流: hub.list(prefix, limit, marker, liveonly)
- Stream
    - [x] 流信息: stream.Info()
    - [x] 禁用流: stream.disable()
    - [x] 启用流: stream.dnable()
    - [x] 查询直播状态: stream.status()
    - [x] 保存直播回放: stream.save(start, end)
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
    - [Stream](#stream)
        - [Get Stream info](#get-stream-info)
        - [Disable a Stream](#disable-a-stream)
        - [Enable a Stream](#enable-a-stream)
        - [Get Stream live status](#get-stream-live-status)
        - [Get Stream history activity](#get-stream-history-activity)
        - [Save Stream live playback](#save-stream-live-playback)

## Installation

before next step, install git.

```
# install latest version
$ pip instal piliv2
```

## Usage

### Configuration

```python
import pili

mac = pili.Mac(AccessKey, SecretKey)
client = pili.Client(mac)

# ...
```

### URL

#### Generate RTMP publish URL

```python
url = pili.rtmp_publish_url("publish-rtmp.test.com", "PiliSDKTest", "streamkey", mac, 60)
fmt.Println(url)
# rtmp://publish-rtmp.test.com/PiliSDKTest/streamkey?e=1463023142&token=7O7hf7Ld1RrC_fpZdFvU8aCgOPuhw2K4eapYOdII:-5IVlpFNNGJHwv-2qKwVIakC0ME=
```

#### Generate RTMP play URL

```python
url = pili.rtmp_play_url("live-rtmp.test.com", "PiliSDKTest", "streamkey")
fmt.Println(url)
# rtmp://live-rtmp.test.com/PiliSDKTest/streamkey
```

#### Generate HLS play URL

```python
url = pili.hls_play_url("live-hls.test.com", "PiliSDKTest", "streamkey")
fmt.Println(url)
# http://live-hls.test.com/PiliSDKTest/streamkey.m3u8
```

#### Generate HDL play URL

```python
url = pili.hdl_play_url("live-hdl.test.com", "PiliSDKTest", "streamkey")
fmt.Println(url)
# http://live-hdl.test.com/PiliSDKTest/streamkey.flv
```

#### Generate Snapshot play URL

```python
url = pili.snapshot_play_url("live-snapshot.test.com", "PiliSDKTest", "streamkey")
fmt.Println(url)
# http://live-snapshot.test.com/PiliSDKTest/streamkey.jpg
```

### Hub

#### Instantiate a Pili Hub object

```python
mac = pili.Mac(AccessKey, SecretKey)
client = pili.Client(mac)
hub = client.hub("PiliSDKTest")
# ...
```

#### Create a new Stream

```python
stream = hub.create(key)

print stream.to_json()
# {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
```

#### Get a Stream

```python
stream = hub.get(key)

print stream.to_json()
# {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
```

#### List Streams

```python
for s in hub.list()["items"]:
    print s.to_json()
# {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
# ...
```

#### List live Streams

```python
for s in hub.list(liveonly=True)["items"]:
    print s.to_json()
# {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
# ...
```

### Stream

#### Get Stream info

```python
print stream.to_json()
# {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
```

#### Disable a Stream

```python
stream.disable()

print stream.to_json()
# before disable: {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
# after disable: {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": -1, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
```

#### Enable a Stream

```python
stream.enable()

print stream.to_json()
# before disable: {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": -1, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
# after disable: {"expireAt": 1465271243, "hub": "PiliSDKTest", "disabledTill": 0, "key": "streamKey", "updatedAt": 1463975243, "createdAt": 1463975243}
```

#### Get Stream live status

```python
print stream.status
# {"startAt": 1463382400, "clientIP": "172.21.1.214:52897" "bps": 128854, "fps": {"audio": 38, "video": 23, "data": 0}}
```

#### Get Stream history activity

```python
print stream.history
# {"items": [{"start": 1463382401, "end": 1463382441}]}
```

#### Save Stream live playback

```python
print stream.save_as()
# {"fname": "recordings/z1.PiliSDKTest.streamkey/1463156847_1463157463.m3u8"}
```
