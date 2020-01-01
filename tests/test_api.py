#!/usr/bin/env python
# coding=utf-8
from app import app
import json


def test_search():
    print('In test_search')
    client = app.test_client()
    rv = client.post('http://localhost:5000/search')
    resp = json.loads(rv.data)
    assert 'ok' == resp['message']
