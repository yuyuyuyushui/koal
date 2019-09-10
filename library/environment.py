from koal import Koal
class Env():
    def __init__(self, api_url, token):
        self.koal = Koal(api_url, token=token)