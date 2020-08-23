import requests
import pytest
import json
import jsonpath
import OpenAuth


@pytest.fixture(scope='session')
def apiauth():
    apiauth = OpenAuth.ApiAuth()
    yield apiauth


def test_openWeatherAPI_CityID(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response 200 and Validate City ID
    response = requests.request('POST', apiurl + 'q=London&' + appid)
    assert response.status_code == 200, 'Requested content(City) found'
    response_json = json.loads(response.text)
    country = jsonpath.jsonpath(response_json, 'sys.country')
    id = jsonpath.jsonpath(response_json, 'id')
    assert id[0] == 2643743, 'Country is id is 2643743'
    lon = jsonpath.jsonpath(response_json, 'coord.lon')
    lat = jsonpath.jsonpath(response_json, 'coord.lat')
    assert lon[0] == -0.13, 'Country is lon is -0.13'
    assert lat[0] == 51.51, 'Country is lat is 51.51'


def test_openWeatherAPI_multiRequest(apiauth):
    # Get the base url
    #apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response count
    response = requests.request('GET', 'http://api.openweathermap.org/data/2.5/group?' + 'id=524901,703448,2643743&units=metric&' + appid)
    assert response.status_code == 200, 'Requested content(Cities) found'
    response_json = json.loads(response.text)
    count = jsonpath.jsonpath(response_json, 'cnt')
    assert count[0] == 3, 'Country returned count value is 3'
    countryCode = jsonpath.jsonpath(response_json, 'list[0].sys.country')
    cityName = jsonpath.jsonpath(response_json, 'list[0].name')
    assert countryCode[0] == 'RU', 'Country is code is RU'
    assert cityName[0] == 'Moscow', 'City name code is Moscow'


def test_openWeatherAPI_multiImperialUnits(apiauth):
    # Get the base url
    #apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response metric untis
    response = requests.request('GET', 'http://api.openweathermap.org/data/2.5/group?' + 'id=1609350&units=imperial&' + appid)
    assert response.status_code == 200, 'Requested content(Cities) found'
    response_json = json.loads(response.text)
    count = jsonpath.jsonpath(response_json, 'cnt')
    assert count[0] == 1, 'Country returned count value is 1'
    metricTemp = jsonpath.jsonpath(response_json, 'list[0].main.temp')
    cityName = jsonpath.jsonpath(response_json, 'list[0].name')
    assert metricTemp[0] > 45, 'City Bangkok ever recodred hottest temp is 40deg c, we are getting the Franhiet and the value retured will be more than 45'
    assert cityName[0] == 'Bangkok', 'City name code is Bangkok'


def test_openWeatherAPI_multiMetricUnits(apiauth):
    # Get the base url
    #apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response metric untis
    response = requests.request('GET', 'http://api.openweathermap.org/data/2.5/group?' + 'id=1609350&units=metric&' + appid)
    assert response.status_code == 200, 'Requested content(Cities) found'
    response_json = json.loads(response.text)
    count = jsonpath.jsonpath(response_json, 'cnt')
    assert count[0] == 1, 'Country returned count value is 1'
    metricTemp = jsonpath.jsonpath(response_json, 'list[0].main.temp')
    cityName = jsonpath.jsonpath(response_json, 'list[0].name')
    assert metricTemp[0] < 45, 'City Bangkok ever recodred hottest temp is 40deg c, we are getting the Franhiet and the value retured will be more than 45'
    assert cityName[0] == 'Bangkok', 'City name code is Bangkok'