import logging, os
class Loger():
    def __init__(self,clevel=logging.INFO, Flevel=logging.DEBUG):
        self.path= os.path.dirname(os.path.dirname(__file__)) + '/log/test.log'
        self.logger = logging.getLogger(self.path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
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
if __name__ =='__main__':
    logyyx = Loger(logging.INFO,logging.DEBUG)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')