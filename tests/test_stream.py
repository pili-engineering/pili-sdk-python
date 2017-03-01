# -*- coding: utf-8 -*-

import os
import random
import time
import unittest

import pili


def env(key):
    if key in os.environ:
        return os.environ[key]
    else:
        return ""


class TestStreamCases(unittest.TestCase):

    def setUp(self):
        hub_name = "PiliSDKTest"
        access_key = env("QINIU_ACCESS_KEY")
        secret_key = env("QINIU_SECRET_KEY")
        if access_key == "" or secret_key == "":
            raise unittest.SkipTest("need set access_key or secret_key")
        if env("PILI_API_HOST") != "":
            pili.conf.API_HOST = env("PILI_API_HOST")
        client = pili.Client(pili.Mac(access_key, secret_key))
        self.hub = client.hub(hub_name)
        self.stream_title = "streamTest" + str(int(random.random()*1e10))

    def test_stream_create(self):
        stream = self.hub.create(self.stream_title)
        self.assertEqual(stream.hub, "PiliSDKTest")
        self.assertEqual(stream.key, self.stream_title)

    def test_stream_disable(self):
        stream = self.hub.create(self.stream_title)
        self.assertFalse(stream.disabled())
        stream.disable()
        stream = stream.refresh()
        self.assertTrue(stream.disabled())
        stream.disable(int(time.time()) + 1)
        stream = stream.refresh()
        self.assertTrue(stream.disabled())
        time.sleep(2)
        stream = stream.refresh()
        self.assertFalse(stream.disabled())

    def test_stream_converts(self):
        stream = self.hub.create(self.stream_title)
        self.assertEqual(len(stream.converts), 0)
        stream.update_converts(["480p", "720p"])
        stream = stream.refresh()
        self.assertEqual(stream.converts, ["480p", "720p"])
        stream.update_converts()
        stream = stream.refresh()
        self.assertEqual(len(stream.converts), 0)

    # 这个测试需要维持推流test1
    def test_stream_saveas(self):
        stream = self.hub.get("test1")
        stream.save_as()
        now = int(time.time())
        stream.save_as(now - 20)
        stream.save_as(now - 20, now)
        ret = stream.save_as(now - 20, now, fname="test1.mp4", format="mp4")
        self.assertEqual(ret["fname"], "test1.mp4")
        self.assertTrue(ret["persistentID"])
        try:
            stream.save_as(now - 20, now, format="mp4", pipeline="notexist")
        except Exception, e:
            self.assertEqual(str(e), "no such pipeline")

    # 这个测试需要维持推流test1
    def test_stream_snashot(self):
        stream = self.hub.get("test1")
        ret = stream.snapshot()
        self.assertTrue(ret["fname"])
        ret = stream.snapshot(fname="test1.jpg")
        self.assertEqual(ret["fname"], "test1.jpg")

    # 这个测试需要维持推流test1
    def test_stream_history(self):
        stream = self.hub.get("test1")
        now = int(time.time())
        ret = stream.history(now - 86400, now)
        self.assertTrue(len(ret) > 0)
        self.assertTrue(ret[0]["start"] > 0)
        self.assertTrue(ret[0]["end"] > 0)
