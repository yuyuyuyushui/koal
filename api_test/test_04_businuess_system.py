from operations.business_system import *
import pytest

business_data=[
    (1, 10),
    (1, 25),
    (1, 50)
]
@pytest.mark.parametrize("page,limit",business_data)
def test_business_system_query_list(env,page,limit):
    env.logger.info("业务系统测试")
    resonse = business_system_list(env.koal, page, limit)
    env.logger.info("业务系统测试的的返回信息{}".format(resonse.response["msg"]))
    assert resonse.success == True, resonse.error
    # assert 0
data = [
    ("124f3610c51c7be86c04a201afaea193",)
]
@pytest.mark.parametrize("abisid",data)
def test_deletbusnisess_system_query_list(env, abisid):
    response = delet_busuness_system(env.koal, abisid)
    assert response.success == True,response.error
if __name__=="__main__":
    pytest.main(["-s", "test_04_businuess_system.py::test_deletbusnisess_system_query_list"])