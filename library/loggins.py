import logging, os,sys
from random import randint
import logging.config

class Loger():
    def __init__(self,clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.path= os.path.dirname(os.path.dirname(__file__)) + '/log/test_path.log'
        self.logger = logging.getLogger(self.path)
        self.logger.setLevel(clevel)
        fmt = logging.Formatter('[%(asctime)s] ---[%(levelname)s]--%(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(self.path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
        self.logger.handlers = self.logger.handlers[:2]
        level = [logging.DEBUG,logging.INFO,logging.WARNING,logging.ERROR,logging.CRITICAL]

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
# def logger_debug(message):
#     return Loger().debug(message)
# def logger_info(message):
#     return Loger().info(message)
# def logger_error(message):
#     return Loger().error(message)

def ranint_name(name):
    newname = '{}_{}'.format(name,randint(0,999))
    return  newname
