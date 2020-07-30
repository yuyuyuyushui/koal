from koal import Koal
from library.loggins import Loger
import os

class Env():
    def __init__(self, api_url,token):
        self.koal = Koal(api_url,token=token)
        self.tool_koal = Koal(api_url)

if __name__ == "__main__":
    pass