import pytest
def test_query_accunt_secret(envi):
    """
    测试获取密码
    :param envi:
    :return:
    """
    param = {
        'page': 1,
        'limit': 10,
        'id': 52,
        'accountId':'36c959922476c7575c710eb1c97ce9ab',
        'secretId':'eecebb0998e8917b5af0b97bd83dc1e3'
    }
    result =envi.ghcatest.assert_accunt_manage.query_password(params=param)
    assert result.response["data"] == 'HGcV27Mvst'
    assert result.success is True
def test_redis(redis):
    a = redis.conn
    print(a)
    assert 0
if __name__ == '__main__':
     pytest.main()