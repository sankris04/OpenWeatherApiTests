import pytest
import json
import jsonpath
import OpenAuth


@pytest.fixture(scope='session')
def apiauth():
    apiauth = OpenAuth.ApiAuth()
    yield apiauth
