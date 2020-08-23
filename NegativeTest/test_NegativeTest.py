import requests
import pytest
import json
import jsonpath
import OpenAuth


#@pytest.fixture(scope='session')
#def apiauth():
 #   apiauth = OpenAuth.ApiAuth()
  #  yield apiauth



def test_openWeatherAPIWrongCountryCode(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Not Found
    response = requests.request('POST', apiurl + 'q=London,DE&' + appid)
    assert response.status_code == 404, 'Requested content(City) not found'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'city not found', 'Requested content(City) not found'


def test_openWeatherAPIBadRequest_NOTCityID(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'id=-0000&' + appid)
    assert response.status_code == 400, '400 Bad Requested'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'Invalid ID', 'Requested ID is not Valid'


def test_openWeatherAPIBadRequest_requestedNOTaCity(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'id=fffff&' + appid)
    assert response.status_code == 400, '400 Bad Requested'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'fffff is not a city ID', 'Requested ID is not a ID'


def test_openWeatherAPIBadRequest_wrongGeoData(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'lon=1&lat=0&' + appid)
    assert response.status_code == 400, '400 Bad Requested'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'Nothing to geocode', 'Requested geocode is not valid'


def test_openWeatherAPIBadRequest_wrongGeoData(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'lon=&lat=0&' + appid)
    assert response.status_code == 400, '400 Bad Requested (GeoData)'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'Nothing to geocode', 'Requested geocode is empty'
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'lon=1&lat=8989898&' + appid)
    assert response.status_code == 400, '400 Bad Requested (wrong lon)'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'wrong latitude', 'Requested wrong latitude'
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'lon=767868&lat=0&' + appid)
    assert response.status_code == 400, '400 Bad Requested(wrong lat)'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'wrong longitude', 'Requested wrong longitude'


def test_openWeatherAPIBadRequest_invalidZipcode(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Bad Request
    response = requests.request('POST', apiurl + 'zip=0,us&' + appid)
    assert response.status_code == 400, '400 Bad Requested(ibvalid zipcode'
    response_json = json.loads(response.text)
    message = jsonpath.jsonpath(response_json, 'message')
    assert message[0] == 'invalid zip code', 'Requested zipcode is not valid'
