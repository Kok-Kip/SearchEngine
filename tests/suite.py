import pytest


class BaseSuite(object):
    @pytest.fixture(autouse=True)
    def init(self, client):
        self.suite = client
        self.client = client.client
        self.app = client.app
