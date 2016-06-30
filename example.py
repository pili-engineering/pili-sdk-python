import pili, time

mac = pili.Mac("AccessKey", "SecretKey")

print pili.rtmp_publish_url("publish-rtmp.test.com", "PiliTest", "streamkey", mac, 60)
print pili.rtmp_play_url("live-rtmp.test.com", "PiliTest", "streamkey")
print pili.hls_play_url("live-rtmp.test.com", "PiliTest", "streamkey")
print pili.hdl_play_url("live-rtmp.test.com", "PiliTest", "streamkey")
print pili.snapshot_play_url("live-rtmp.test.com", "PiliTest", "streamkey")

client = pili.Client(mac)
hub = client.hub("PiliTest")

ss = hub.list(liveonly=True)
for i in ss["items"]:
    print i.key

stream = hub.get("test1234")
print stream.to_json()

stream.disable()
print stream.refresh().to_json()

stream.enable()
print stream.refresh().to_json()

print stream.status()

print stream.history()

print stream.saveas()
