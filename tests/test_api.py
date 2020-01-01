#!/usr/bin/env python
# coding=utf-8
import pytest

def test_app():
    assert 5 == 5
'''
@pytest.fixture()
def client():
    test_client = app.test_client()
    yield  test_client

def test_search(client):
    rv = client.post('htpps://localhost:5000/search')
'''

if __name__ == "__main__":
    pytest.main()