#!/usr/bin/env python
# coding=utf-8
import pytest
from app import app
import json

def test_app():
    assert 5 == 5


@pytest.fixture
def client():
    test_client = app.test_client()
    yield test_client


def test_search(client):
    rv = client.post('http://127.0.0.1:5000/search')
    resp = json.loads(rv.data)
    assert 'ok' == resp["message"]


if __name__ == "__main__":
    pytest.main()
