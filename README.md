pili-python
===========

pili-io Python SDK

Usage:
-------------
    hub = Hub(access_key = access_key, secret_key = secret_key, hub_name = name)

    res = hub.create_stream();

    print "get_stream_list"
    for x in hub.streams():
        print x.id

    print "get_stream"
    for x in hub.streams():
        print hub.get_stream(stream_id=x.id).id

    print "update_stream"
    for x in hub.streams():
        x.update(publishKey = "1")
    for x in hub.streams():
        print x.id, x.publishKey

    print "get_segments"
    for x in hub.streams():
        print x.id, x.get_segments(start_second=0, end_second=1000)

    print "delete_stream"
    for x in hub.streams():
        x.delete()
    for x in hub.streams():
        print "Error!", x.id
    print "should be nothing."
