# -*- coding: utf-8 -*-

import os
import unittest

import pili


def env(key):
    if key in os.environ:
        return os.environ[key]
    else:
        return ""


class TestHubCases(unittest.TestCase):

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

    # 这个测试case需要保持推流test1
    def test_batch_live_status(self):
        items = self.hub.batch_live_status(["test1", "test2"])
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["key"], "test1")
        self.assertTrue(items[0]["startAt"] > 0)
        self.assertTrue(items[0]["bps"] > 0)
