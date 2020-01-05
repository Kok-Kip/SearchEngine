import pytest
from app.biz.common import add_dict
import numpy as np

def test_add_dict():
    x1 = {"key1": 5, "key2": 8}
    y1 = {"key1": 10, "key2": 1}
    add_dict(x1, y1)
    assert y1["key1"] == 15
    assert y1["key2"] == 9

    x2 = {"key1": 5, "key2": 8}
    y2 = {"key1": 1, "key3": 10}
    add_dict(x2, y2)
    assert y2["key1"] == 6
    assert y2["key2"] == 8
    assert y2["key3"] == 10
