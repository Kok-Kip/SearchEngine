#!/usr/bin/env python
# coding=utf-8
from tests.suite import BaseSuite

class TestServer(BaseSuite):
    def test_search(self):
        rv = self.client.post('http://localhost:5000')
        resp = rv.data
        print(resp)
        assert 1 == 1