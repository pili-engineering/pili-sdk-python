import unittest
import pytest
import pili.auth

class AuthTestCase(unittest.TestCase):

    def test_auth_interface_str(self):
        a = pili.auth.Auth('1234567890', '0987654321')
        assert 'Qiniu 1234567890:tDCk2v-dSc9U86BGV3EjDDpnswY=' == a.auth_interface_str("abcd")

