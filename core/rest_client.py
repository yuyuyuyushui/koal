import requests,urllib3



from core.base import *

class RestClient():

    def __init__(self, api_url_path, token=None):
        self.session = requests.session()
        self.session.headers["Content-Type"] = "application/json"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if token:
            self.session.headers['token'] = token
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

