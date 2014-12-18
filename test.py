from pili import *

access_key = 'xW8BESy2EUIN-97PwNiKrzlYgZZohSW_5X5402lAwbg='
secret_key = '88HScKCal6GQ_0EQt0zAkiFzkelp0C7aX7U-emz82bzu_DZTFmCfT-3b37OKo0rMDw4FnO80EyqJ6_WAMXjMSw=='

a = Auth(access_key = access_key, secret_key = secret_key)
#print create_stream(a, stream_key = '548fd153938a7c0007000007')
#print get_stream_list(a)
#print get_stream(a, id = '548fd153938a7c0007000007')
#print update_stream(a, id = '548fd153938a7c0007000007', is_private = True)
#print delete_stream(a, id = '548fd153938a7c0007000007')
print get_stream_status(a, id = '5492707fcbc3180007000001')