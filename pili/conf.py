"""
Settings
"""
import platform
import sys


API_VERSION = 'v2'
API_HOST = 'pili.qiniuapi.com'

API_USERAGENT = "pili-sdk-python/v2 %s %s" % (platform.python_version(), sys.platform)
