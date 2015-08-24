# Pili Streaming Cloud server-side library for Python

## Features

- Stream Create,Get,List
    - [x] hub.create_stream()
    - [x] hub.get_stream()
    - [x] hub.list_streams()
- Stream operations else
    - [x] stream.to_json()
    - [x] stream.update()
    - [x] stream.disable()
    - [x] stream.enable()
    - [x] stream.status()
    - [x] stream.rtmp_publish_url()
    - [x] stream.rtmp_live_urls()
    - [x] stream.hls_live_urls()
    - [x] stream.http_flv_live_urls()
    - [x] stream.segments()
    - [x] stream.hls_playback_urls()
    - [x] stream.snapshot()
    - [x] stream.save_as()
    - [x] stream.delete()


## Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Configuration](#configuration)
    - [Hub](#hub)
        - [Instantiate a Pili Hub object](#instantiate-a-pili-hub-object)
        - [Create a new Stream](#create-a-new-stream)
        - [Get a Stream](#get-a-stream)
        - [List Streams](#List-streams)
    - [Stream](#stream)
        - [To JSON string](#to-json-string)
        - [Update a Stream](#update-a-stream)
        - [Disable a Stream](#disable-a-stream)
        - [Enable a Stream](#enable-a-stream)
        - [Get Stream status](#get-stream-status)
        - [Generate RTMP publish URL](#generate-rtmp-publish-url)
        - [Generate RTMP live play URLs](#generate-rtmp-live-play-urls)
        - [Generate HLS live play URLs](generate-hls-live-play-urls)
        - [Generate Http-Flv live play URLs](generate-http-flv-live-play-urls)
        - [Get Stream segments](#get-stream-segments)
        - [Generate HLS playback URLs](generate-hls-playback-urls)
        - [Save Stream as a file](#save-stream-as-a-file)
        - [Snapshot Stream](#snapshot-stream)
        - [Delete a Stream](#delete-a-stream)
- [History](#history)


## Installation

```shell
pip install pili
# Note: The interface has changed after version 1.2.
#       If you need deprecated API, use pip install -v pili==0.1.0.
```

## Usage:

### Configuration

```python
from pili import *

access_key = 'qiniu_access_key' 
secret_key = 'qiniu_secret_key'

hub_name   = 'pili_hub_name' # The Hub must be exists before use

# Change API host as necessary
# 
# pili.qiniuapi.com as deafult
# pili-lte.qiniuapi.com is the latest RC version
# 
conf.API_HOST = 'pili-lte.qiniuapi.com'
```

### Hub

#### Instantiate a Pili Hub object

```python
credentials = Credentials(access_key, secret_key)
hub = Hub(credentials, hub_name)
```

#### Create a new Stream

```python
# title          : optional, string, auto-generated as default
# publishKey     : optional, string, auto-generated as default
# publishSecrity : optional, string, can be "dynamic" or "static", "dynamic" as default
stream = hub.create_stream(title=None, publishKey=None, publishSecurity="static")
# return stream object...
```

#### Get a Stream

```python
# stream_id: required, string
stream = hub.get_stream(stream_id=id)
# return stream object...
```

#### List Streams

```python
# marker : optional, string
# limit  : optional, int
# title  : optional, string
res = hub.list_streams(marker=None, limit=50, title="prefix_")
for s in res["items"]:
    # s is stream object...
    # Do someting...
    pass
next = hub.list_streams(marker=res["marker"])
```

### Stream

#### To JSON string

```python
stream.to_json()
```

#### Update a Stream

```python
# publishKey     : optional, string
# publishSecrity : optional, string
# disabled       : optional, bool
stream.update(publishKey = "new_secret_words", publishSecurity="dynamic")
```

#### Disable a Stream

```python
stream.disable()
```

#### Enable a Stream

```python
stream.enable()
```

#### Get Stream status

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

#### Generate RTMP publish URL

```python
url = stream.rtmp_publish_url()
print url
```

#### Generate RTMP live play URLs

```python
urls = stream.rtmp_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original RTMP live url
original_url = urls["ORIGIN"]
```

#### Generate HLS play live URLs

```python
urls = stream.hls_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original HLS live url
original_url = urls["ORIGIN"]
```

#### Generate Http-Flv live play URLs

```python
urls = stream.http_flv_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original Http-Flv live url
original_url = urls["ORIGIN"]
```

#### Get Stream segments

```python
# start : optional, int64, in second, unix timestamp
# end   : optional, int64, in second, unix timestamp
# limit : optional, uint32
# ...but you must provide both or none of the arguments.
segments = stream.segments(start_second=start, end_second=end, limit=None)
print segments
# [
#     {
#         "start": <StartSecond>,
#         "end": <EndSecond>
#     },
#     {
#         "start": <StartSecond>,
#         "end": <EndSecond>
#     },
#     ...
# ]
```

#### Generate HLS playback URLs

```python
# start : required, int64, in second, unix timestamp
# end   : required, int64, in second, unix timestamp
urls = stream.hls_playback_urls(start, end)
for k in urls:
    print k, ":", urls[k]

# Get original HLS playback url
original_url = urls["ORIGIN"]
```

#### Save Stream as a file

```python
# name      : required, string
# format    : required, string, see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# start     : required, int64, in second, unix timestamp
# end       : required, int64, in second, unix timestamp
# notifyUrl : optional, string 
res = stream.save_as(name="videoName.mp4", format="mp4", start_second=start, end_second=end, notifyUrl=None)
print res
# {
#     "url": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.m3u8",
#     "targetUrl": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.mp4",
#     "persistentId": "z1.55d81c6c7823de5a49ad77b3"
# }
```

#### Snapshot stream
```python
# name      : required, string
# format    : required, string see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# time      : optional, int64, in second, unix timestamp
# notifyUrl : optional, string 
res = stream.snapshot(name="imageName.jpg", format="jpg", time=None, notifyUrl=None)
print res
# {
#     "targetUrl": "http://ey636h.static1.z1.pili.qiniucdn.com/snapshots/z1.test-hub.55d81a72e3ba5723280000ec/imageName.jpg",
#     "persistentId": "z1.55d81c247823de5a49ad729c"
# }
```

While invoking `saveAs()` and `snapshot()`, you can get processing state via Qiniu FOP Service using `persistentId`.  
API: `curl -D GET http://api.qiniu.com/status/get/prefop?id={PersistentId}`  
Doc reference: <http://developer.qiniu.com/docs/v6/api/overview/fop/persistent-fop.html#pfop-status>  

#### Delete a stream
```python
stream.delete()
```

## History

