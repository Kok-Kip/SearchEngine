#!/usr/bin/env python
# coding=utf-8
from app import app
import json
import pytest


@pytest.fixture
def client():
    test_client = app.test_client()
    yield test_client


def test_search(client):
    print('In test_search')
    client = app.test_client()
    rv = client.post('http://localhost:5000/search')
    resp = json.loads(rv.data)
    assert 'ok' == resp['message']
