import redis
host='10.11.132.131'
port = '7521'
passwd = 'tha#hoh_Nau6'


def redis_conn():
    pool = redis.ConnectionPool(host=host,port=port,password=passwd)
    return redis.Redis(connection_pool=pool)


def delete_keys(keys):
    pool = redis.ConnectionPool(host=host, port=port, password=passwd)
    conn = redis.Redis(connection_pool=pool)
    keys = conn.keys(keys)
    for key in keys:
        conn.delete(key)
    return conn


class RedisConnet:
    def __init__(self, host, port, passwd):
        try:
            self.conn = redis.Redis(connection_pool=redis.ConnectionPool(host=host, port=port, password=passwd))
        except Exception as e:
            print(e)

    def detete_keys(self, keys):
        """
        循环删除keys
        :param keys:
        :return:
        """
        keys = self.conn.keys(keys)
        for key in keys:
            self.conn.delete(key)
        return self.conn
if __name__=="__main__":
    conn = redis_conn()
    print(conn.keys('login:fail:ip:*'))