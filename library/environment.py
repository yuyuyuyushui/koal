from koal import Koal
from library.loggins import Loger
import os

class Env():
    log_path = os.path.dirname(os.path.dirname(__file__)) + '/log/test.log'
    def __init__(self, api_url, token):
        self.koal = Koal(api_url, token=token)
        self.logger = Loger(Env.log_path)
if __name__ == "__main__":
    pass