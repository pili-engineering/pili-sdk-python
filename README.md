pili-sdk-python
=============

Pili server-side library for Python.

Installation
-------------
Install it from pip

    $ pip install pili

Usage:
-------------
### Init Setup
```python
from pili import *

clt = Client(access_key, secret_key, hub_name)
```

### Create Stream

```python
clt.create_stream()
```
or you can specify some arguments like

```python
clt.create_stream(title="test", publishSecurity="static")
```

### Get Stream
```python
stream = clt.get_stream(stream_id=id)
```

### Update Stream
```python
stream.update(publishSecurity="dynamic")
```
...or
```python
stream.update(publishKey = key)
```
...or
```python
stream.update(publishKey = key, publishSecurity="dynamic")
```

### Delete Stream
```python
stream.delete()
```

### Get Stream List
```python
res = clt.list_streams()
for s in res["items"]:
    pass
next = clt.list_streams(marker=res["marker"])
```

### Get Stream Segments
```python
stream.segments(start_second=start, end_second=end)
```

### Get Stream RTMP Live URL

```python
stream.rtmp_live_url()
```

### Get Stream HLS Live URL

```python
stream.hls_live_hls()
```
    
### Get Stream HLS Playback URL

```python
stream.hls_playback_url(start, end)
```

### Get Stream RTMP Publish URL

```python
stream.rtmp_publish_url()
```
or if you want to specify the `nonce` when using `dynamic`
```python
stream.rtmp_publish_url(nonce="1")
```
