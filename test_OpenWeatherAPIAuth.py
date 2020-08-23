import requests
import pytest
import OpenAuth


@pytest.fixture(scope='session')
def apiauth():
    apiauth = OpenAuth.ApiAuth()
    yield apiauth


@pytest.mark.Smoke
@pytest.mark.Regression
def test_openWeatherAPIAuthSuccessResponse(apiauth):
    # Get the base url

    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response code 200
    response = requests.request('GET',apiurl+'q=London&'+appid)
    assert response.status_code == 200, 'Response Code Should be 200'


def test_openWatherAPIAuthFailreResponse(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the invalid appid
    invalidappid = apiauth.invalidappid_key()
    # Validate the Response code 401
    response = requests.request('GET',apiurl+'q=London&'+invalidappid)
    assert response.status_code == 401, 'Response Code Should be 401'
    print(response.json())




def test_openWatherAPIAuthHeaderResponse(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the invalid appid
    appid = apiauth.appid_key()
    # Validate the Response code 401
    response = requests.request('GET',apiurl+'q=London&'+appid)
    assert response.headers['Content-Type'] == "application/json; charset=utf-8",'Header Content-Type Should be application/json'
    assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST', 'Header Allowed menthods Should be GET and POST'
    assert response.headers['Access-Control-Allow-Credentials'] == 'true', 'Header Allowed Credtials Should be True'


