import os
from configparser import ConfigParser


class ApiAuth:
    'Common base class for all API'
    empCount = 0

    def __init__(self):
        self.file = 'appconfig/config.ini'

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


