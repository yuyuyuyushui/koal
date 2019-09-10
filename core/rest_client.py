import requests


class RestClient():
    def __init__(self, api_url_path, username=None,password=None,token=None,**kwargs):
        self.session = requests.session()
        if username and password:
            self.session.auth = (username, password)
        elif token:
            # print(self.session.headers)
            # self.session.headers.update({'token':token})
            self.session.headers['token']=token
            # print(self.session.headers)
            # self.session.headers['Content-Type'] = "application/json"
            # self.session.headers['Cookie'] = "JSESSIONID=B1B4E5526A70DB45EAF810BAC73237F0"
            # print(self.session.headers)
        else:
             print('输入有误')
        self.api_url_path = api_url_path

    def get(self, url, **kwargs):
        url = self.api_url_path + url
        # print(url)
        # print(self.session.headers)
        #re = self.session.request('get', 'http://10.143.220.117:9090/v1/dept/list')
        # print(re.text)
        return self.session.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        url = self.api_url_path + url
        # s = requests.session().get(url)
        # print(s.text)

        return self.session.request('post', url, **kwargs)

    def patch(self,url,**kwargs):
        url = self.api_url_path +url
        return self.session.request('patch', url, **kwargs)

    def put(self,url,**kwargs):
        url = self.api_url_path+url
        return self.session.request('put', url, **kwargs)

    def delete(self, url, **kwargs):
        url = self.api_url_path+url
        return self.session.request('delete',url,**kwargs)

