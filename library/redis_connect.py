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
if __name__=="__main__":
    conn = redis_conn()

    # print(conn.get("login:fail:ip:10.1.6.81:"))
    # conn.delete("login:fail:ip:")
    # print(conn.get("login:fail:ip:"))
    print(conn.keys('login:fail:ip:*'))