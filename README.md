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

```
$ pip install pili
```

## Usage:

### Client

#### Create a Pili client

```python
from pili import *

access_key = 'qiniu_access_key' 
secret_key = 'qiniu_secret_key'
hub_name   = 'hub_name'

clt = Client(access_key, secret_key, hub_name)
```

#### Create a stream

```python
# title          : optional
# publishKey     : optional
# publishSecrity : optional
clt.create_stream(title="test", publishKey="abc", publishSecurity="static")
```

#### Get a stream

```python
# stream_id: required
stream = clt.get_stream(stream_id=id)
```

#### List streams
```python
# marker : optional
# limit  : optional
res = clt.list_streams()
for s in res["items"]:
    # Do someting...
    pass
next = clt.list_streams(marker=res["marker"])
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
stream.status()
```

#### Get stream segments
```python
# start : optional
# end   : optional
# ...but you must provide both or none of the arguments.
stream.segments(start_second=start, end_second=end)
```

#### Generate RTMP publish URL
```python
stream.rtmp_publish_url()
```

#### Generate RTMP live play URL
```python
stream.rtmp_live_urls()
```

#### Generate HLS live play URL
```python
stream.hls_live_urls()
```
    
#### Generate HLS playback URL

```python
stream.hls_playback_urls(start, end)
```

