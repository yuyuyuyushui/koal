import logging, os
class Loger():
    def __init__(self,clevel=logging.INFO, Flevel=logging.INFO):
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


class a():
    def __init__(self):
        self.a = 1

    def test(self, message):
        print(message)


if __name__ =='__main__':
    a().test(33)
    a().test(55)