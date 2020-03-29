import requests
from core.base import *

class RestClient1():
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
    # def __init__(self,api_url_path,**kwargs):
    #     self.session = requests.session()
    #     self.api_url_path = api_url_path
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
class RestClient2():
    # def __init__(self, api_url_path, username=None,password=None,token=None,**kwargs):
    #     self.session = requests.session()
    #
    #     if username and password:
    #         self.session.auth = (username, password)
    #     elif token:
    #         self.session.headers['token']=token
    #
    #     else:
    #          print('输入有误')
    #     self.api_url_path = api_url_path
    #     self.url = None
    def __init__(self,api_url_path,**kwargs):
        self.session = requests.session()
        self.api_url_path = api_url_path
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
