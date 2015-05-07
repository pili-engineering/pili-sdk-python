pili-python
=============

Pili SDK for Python

Installation
-------------
Install it from pip

    $ pip install pili

Usage:
-------------
### Setup Hub
```python
from pili import Hub

hub = Hub(access_key = access_key, secret_key = secret_key, hub_name = name)
```

### Create Stream

```python
hub.create_stream()
```
or you can specific some arguments like

```python
hub.create_stream(title="test", publishSecurity="static")
```

### Get Stream
```python
stream = hub.get_stream(stream_id=id)
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
for s in hub.stream():
    pass
```

### Get Stream Segments
```python
stream.get_segments(start_second=start, end_second=end)
```

## Get Stream RTMP Live URL

```python
stream.play.rtmp_live()
stream.play.rtmp_live(profile="480p")
```

You can change RTMP play host by

```python
stream.play.rtmp_play_host = host
```

### Get Stream HLS Live URL

```python
stream.play.hls_live()
stream.play.hls_live(profile="480p")
```

You can change HLS play host by

```python
stream.play.hls_play_host = host
```
    
### Get Stream HLS Playback URL

```python
stream.play.hls_playback(start, end)
stream.play.hls_playback(start, end, profile="480p")
```

You can change HLS play host by

```python
stream.play.hls_play_host = host
```

## Get Stream RTMP Publish URL

```python
stream.publish.url()
```
or if you want to specificate the `nonce` when using `dynamic`
```python
stream.publish.url(nonce="1")
```

You can change RTMP publish host by

```python
stream.play.rtmp_publish_host = host
```
