from pili import *

access_key = 'x5PTzM4gEy-vqaEicIwDIEdakkOffL7iHptSHFID'
secret_key = 'WJ82-ye5UC8Sa8vEkdH5yAs6XIgZlnoTMe9qWnCU'
hub = "test-sdk"

#conf.API_HOST = "staging.pili.qiniudns.com"
clt = Client(access_key, secret_key, hub)


res = clt.create_stream(publishSecurity="static");

print "get_stream_list"
res = clt.list_streams()
for x in res["items"]:
    print x.id

for x in res["items"]:
    print x.rtmp_live_url()

print "get_stream"
for x in res["items"]:
    print x.status()
    print clt.get_stream(stream_id=x.id).id

print "update_stream"
for x in res["items"]:
    x.update(publishKey = "1", publishSecurity="dynamic")
for x in res["items"]:
    x.refresh()
    print x.id, x.publishKey
    print x.rtmp_publish_url()

print "get_segments"
for x in res["items"]:
    print x.id, x.segments()

print "delete_stream"
for x in res["items"]:
    x.delete()
