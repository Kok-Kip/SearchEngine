import pytest
from app.app import create_app


class Client(object):
    def __init__(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def clean(self):
        return


@pytest.fixture(scope='function')
def client(request):
    client = Client()
    request.addfinalizer(client.clean)
    return client
