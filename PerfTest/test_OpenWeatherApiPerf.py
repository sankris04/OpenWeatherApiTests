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
    assert response.elapsed.total_seconds() <= 0.0250, "Response elpased time should be less than 250 ms"

def test_openWeatherAPIAuthPrallelRequest(apiauth):
    # Get the base url
    apiurl = apiauth.base_url()
    # Get the appid
    appid = apiauth.appid_key()
    # Validate Response Time

    with requests.Session() as session:
        session.get(apiurl + 'q=London&' + appid)


