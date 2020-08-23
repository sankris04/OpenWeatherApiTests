import requests
import pytest



def test_openWeatherAPIAuthResponseTime(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Time
    response = requests.request('POST', apiurl + 'q=London&' + appid)
    print(response.elapsed.total_seconds())
    assert response.elapsed.total_seconds() <= 1000, "Response elpased time should be less than 250 ms"