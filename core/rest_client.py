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

    @response
    def get(self, url, **kwargs):
        self.api_url_path = self.api_url_path + url
        return self.session.request('get', self.api_url_path, **kwargs)

    @response
    def post(self, url, **kwargs):
        self.api_url_path = self.api_url_path + url
        # s = requests.session().get(url)
        # print(s.text)
        # print(self.session.params)
        return self.session.request('post', self.api_url_path, **kwargs)

    @response
    def patch(self,url,**kwargs):
        self.api_url_path = self.api_url_path +url
        return self.session.request('patch', self.api_url_path, **kwargs)

    @response
    def put(self, url, **kwargs):
        self.api_url_path = self.api_url_path+url
        return self.session.request('put', self.api_url_path, **kwargs)

    @response
    def delete(self, url, **kwargs):
        self.api_url_path = self.api_url_path + url
        # print(url)
        return self.session.request('delete', self.api_url_path, **kwargs)

