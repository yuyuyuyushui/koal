import requests
from core.base import *

class RestClient():
    def __init__(self, api_url_path, username=None,password=None,token=None,**kwargs):
        self.session = requests.session()
        if username and password:
            self.session.auth = (username, password)
        elif token:
            self.session.headers['token']=token

        else:
             print('输入有误')
        self.api_url_path = api_url_path
        self.url = None

    @response
    def get(self, url, **kwargs):
        self.url = self.api_url_path + url
        return self.session.request('get', self.url, verify = False,**kwargs)

    @response
    def post(self, url, **kwargs):
        self.url = self.api_url_path + url
        return self.session.request('post', self.url, verify = False, **kwargs)

    @response
    def patch(self,url,**kwargs):
        self.url = self.api_url_path +url
        return self.session.request('patch', self.url, verify = False,**kwargs)

    @response
    def put(self, url, **kwargs):
        self.url = self.api_url_path+url
        return self.session.request('put', self.url, verify = False, **kwargs)

    @response
    def delete(self, url, **kwargs):
        self.url = self.api_url_path + url
        return self.session.request('delete', self.url,verify = False, **kwargs)

