from operations.business_system import *
import pytest
from core.base import *

business_data=[
    (1, 10),
    # (1, 25),
    # (1, 50)
]
@pytest.mark.parametrize("page,limit",business_data)
def test_business_system_query_list(env, page, limit):
    logger_info("测试业务系统查询列表")
    resonse = Business_system_api(env.koal).business_system_list(page, limit)
    # env.logger.info("业务系统测试的的返回信息{}".format(resonse.response["msg"]))
    assert resonse.success == True, resonse.error
    # assert 0
data = [
    ("ae1eebcea5cfdab1ef329d64846cda5f")
]


@pytest.mark.parametrize("abisid",data)
def test_deletbusnisess_system_query_list(env, abisid):
    print(abisid)
    response = Business_system_api(env.koal).delet_busuness_system(abisid)
    assert response.success == True, response.error
    assert 0

if __name__=="__main__":
    pytest.main(["-s", "test_04_businuess_system.py::test_business_system_query_list"])