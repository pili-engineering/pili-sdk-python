# Pili server-side library for Python.

## Features

- [x] Stream operations (Create, Delete, Update, Get)
- [x] Get Streams list
- [x] Get Stream status
- [x] Get Stream segments
- [x] Generate RTMP publish URL
- [x] Generate RTMP / HLS live play URL
- [x] Generate HLS playback URL

## Content

- [Installation](#installation)
- [Usage](#usage)
    - [Client](#client)
        - [Create a Pili client](#create-a-pili-client)
        - [Create a stream](#create-a-stream)
        - [Get a stream](#get-a-stream)
        - [List streams](#list-streams)
    - [Stream](#stream)
        - [Update a stream](#update-a-stream)
        - [Delete a stream](#delete-a-stream)
        - [Get stream segments](#get-stream-segments)
        - [Get stream status](#get-stream-status)
        - [Generate RTMP publish URL](#generate-rtmp-publish-url)
        - [Generate RTMP live play URL](#generate-rtmp-live-play-url)
        - [Generate HLS live play URL](#generate-hls-live-play-url)
        - [Generate HLS playback URL](#generate-hls-playback-url)

## Installation

```shell
pip install pili
# Note: The interface has changed after version 1.2.
#       If you need deprecated API, use pip install -v pili==0.1.0.
```

## Usage:

### Client

#### Create a Pili client

```python
from pili import *

access_key = 'qiniu_access_key' 
secret_key = 'qiniu_secret_key'
hub_name   = 'hub_name'

client = Client(access_key, secret_key, hub_name)
```

#### Create a stream

```python
# title          : optional
# publishKey     : optional
# publishSecrity : optional
stream = client.create_stream(title="test", publishKey="abc", publishSecurity="static")
# return stream object...
```

#### Get a stream

```python
# stream_id: required
stream = client.get_stream(stream_id=id)
# return stream object...
```

#### List streams
```python
# marker : optional
# limit  : optional
res = client.list_streams()
for s in res["items"]:
    # s is stream object...
    # Do someting...
    pass
next = client.list_streams(marker=res["marker"])
```

### Stream

#### Update a stream
```python
# publishKey     : optional
# publishSecrity : optional
# disabled       : optional
stream.update(publishKey = key, publishSecurity="dynamic")
```

#### Delete a stream
```python
stream.delete()
```

#### Get stream status
```python
status = stream.status()
print status
# {
#     "addr": "106.187.43.211:51393",
#     "status": "disconnected"
# }
```

#### Get stream segments
```python
# start : optional
# end   : optional
# ...but you must provide both or none of the arguments.
segments = stream.segments(start_second=start, end_second=end)
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

#### Generate RTMP publish URL
```python
url = stream.rtmp_publish_url()
print url
```

#### Generate RTMP live play URL
```python
urls = stream.rtmp_live_urls()
for k in urls:
    print k, ":", urls[k]
```

#### Generate HLS live play URL
```python
urls = stream.hls_live_urls()
for k in urls:
    print k, ":", urls[k]
```
    
#### Generate HLS playback URL

```python
urls = stream.hls_playback_urls(start, end)
for k in urls:
    print k, ":", urls[k]
```

