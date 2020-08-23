import os
import json
from configparser import ConfigParser


class ApiAuth:
    'Common base class for all API'
    empCount = 0

    def __init__(self) -> object:
        self.file = 'appconfig/config.ini'
        self.data = None

    def base_url(self):
        config = ConfigParser()
        config.read(self.file)
        baseurl = config['BaseUrl']['url']
        return baseurl

    def appid_key(self):
        config = ConfigParser()
        config.read(self.file)
        appid = config['Key']['appid']
        return appid

    def invalidappid_key(self):
        config = ConfigParser()
        config.read(self.file)
        invalidappid = config['Key']['invalidappid']
        return invalidappid

    def read_jsonfile(self):
        #citiesjsonfile = open('cities.json', 'r')
        with open('cities.json','r') as f:
            jsondata = f.read()
        return jsondata


