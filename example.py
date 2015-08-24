from pili import *

access_key = "Qiniu_AccessKey"
secret_key = "Qiniu_SecretKey"
hub_name   = "Pili_Hub_Name" # The Hub must be exists before use

# Change API host as necessary
# 
# pili.qiniuapi.com as deafult
# pili-lte.qiniuapi.com is the latest RC version
# 
conf.API_HOST = 'pili-lte.qiniuapi.com'

credentials = Credentials(access_key, secret_key)
hub = Hub(credentials, hub_name)

# Create a new Stream
# title          : optional, string, auto-generated as default
# publishKey     : optional, string, auto-generated as default
# publishSecrity : optional, string, can be "dynamic" or "static", "dynamic" as default
stream = hub.create_stream()
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

# Get Stream
# stream_id: required, string
stream = hub.get_stream(stream.id)
print "\nget_stream()\n", stream.to_json()
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

# List streams
# marker : optional, string
# limit  : optional, int
# title  : optional, string
print "\nlist_streams()\n", hub.list_streams()
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

# Update a Stream
# publishKey     : optional, string
# publishSecrity : optional, string
# disabled       : optional, bool
stream.update(publishKey = "new_secret_words", publishSecurity="static")
print "\nStream update()\n", stream.to_json()
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

# Disable a Stream
stream.disable()
print "\nStream disable()\n", "disabled:", stream.disabled

# Enable a Stream
stream.enable()
print "\nStream enable()\n", "disabled:", stream.disabled

# Get Stream status
print "\nStream status()\n", stream.status()
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

# Generate RTMP publish URL
print "\nStream rtmp_publish_url()\n", stream.rtmp_publish_url()
# rtmp://e4kvkh.publish.z1.pili.qiniup.com/test-origin/55db52e1e3ba573b2000000e?key=new_secret_words

# Generate RTMP live play URLs
print "\nStream rtmp_live_urls()\n", stream.rtmp_live_urls()
# {"ORIGIN": "rtmp://e4kvkh.live1-rtmp.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e"}

# Generate HLS play URLs
print "\nStream hls_live_urls()\n", stream.hls_live_urls()
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.m3u8"}

# Generate Http-Flv live play URLs
print "\nStream http_flv_live_urls()\n", stream.http_flv_live_urls()
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.flv"}

# Get Stream segments
# start_second : optional, int64, in second, unix timestamp
# end_second   : optional, int64, in second, unix timestamp
# limit        : optional, uint32
# ...but you must provide both or none of the arguments.
print "\nStream segments()\n", stream.segments()
# [
#     {
#         "start": 1440282134,
#         "end": 1440437833
#     },
#     {
#         "start": 1440437981,
#         "end": 1440438835
#     }
# ]

# Generate HLS playback URLs
# start = 1440282134 : required, int64, in second, unix timestamp
# end   = 1440437833 : required, int64, in second, unix timestamp
print "\nStream hls_playback_urls(1440282134, 1440437833)\n", stream.hls_playback_urls(start, end)
# {"ORIGIN": "http://e4kvkh.playback1.z1.pili.qiniucdn.com/test-origin/55db5699e3ba573b20000010.m3u8?start=1440282134&end=1440437833"}

# Save Stream as a file
# name      : required, string
# format    : required, string, see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# start     : required, int64, in second, unix timestamp
# end       : required, int64, in second, unix timestamp
# notifyUrl : optional, string 
res = stream.save_as(name="videoName.mp4", format="mp4", start=1440282134, end=1440437833, notifyUrl=None)
print res
# {
#     "url": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-origin.55db5699e3ba573b20000010/videoName.m3u8",
#     "targetUrl": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-origin.55db5699e3ba573b20000010/videoName.mp4",
#     "persistentId": "z1.55d81c6c7823de5a49ad77b3"
# }

# Snapshot stream
# name      : required, string
# format    : required, string see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# time      : optional, int64, in second, unix timestamp
# notifyUrl : optional, string 
res = stream.snapshot(name="imageName.jpg", format="jpg", time=None, notifyUrl=None)
print res
# {
#     "targetUrl": "http://ey636h.static1.z1.pili.qiniucdn.com/snapshots/z1.test-origin.55db5699e3ba573b20000010/imageName.jpg",
#     "persistentId": "z1.55d81c247823de5a49ad729c"
# }

# Delete a Stream
stream.delete()
