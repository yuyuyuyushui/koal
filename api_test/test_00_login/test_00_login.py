import pytest
from random import randint
from library.loggins import *
from operations.access_audit import *
from operations.login import *
from library.redis_connect import *
import allure
from koal import Koal
from library.Data import *


# url = Data.UrlPath

@allure.feature("测试正常登录")
def test_login_nomal(envi, loginname='admin', password='ghcatest'):
    logger_debug('测试正常登录')

    result = loging(envi,loginname,password)
    assert result.success is True, result.error

    result_access = access_audit_query(envi.admin)
    assert result_access.success, result_access.errors


@allure.feature("测试连续登录四次登录失败")
def test_logining_four_false(envi,redis, loginname='ghca', password='11'):
    logger_debug("测试连续登录四次登录失败")
    four_result=login_times(envi,loginName=loginname,password=password, times=4)
    assert four_result[0].success is False
    assert four_result[3].response["msg"] == '连续登录失败,用户帐号被禁用'

    result_query = access_audit_query(envi.admin)
    assert result_query.success is True,result_query.error

    result_delete = delet_access_audit(envi.admin, key=result_query.response["data"][0]["key"])
    assert result_delete.success is True
    redis.detete_keys("login:fail:*")

    result_query_none = access_audit_query(envi.admin)
    assert result_query_none.response["data"] == []

    result_five = login_times(envi, loginName=loginname, password="111111", times=1)
    assert result_five[0].success is True, result_five.error

@allure.feature("测试连续登录失败5次，IP地址被禁用")
def test_loging_five_flse_and_ip_forbidden(envi):
    logger_debug("测试连续登录失败5次，IP地址被禁用")
    """
    先登录失败，再查询登录失败，再删除失败登录，最后正确登录
    """
    login_false_list = login_times(envi, loginName='ghca', password='111', times=3)
    assert login_false_list[2].success is False

    result_login_false_list = login_times(envi, loginName='liulj', password='111', times=2)
    assert result_login_false_list[1].response['msg'] == '连续登录失败,IP被禁用'

    result_ip = access_audit_query(envi.admin)
    assert result_ip.success is True
    assert result_ip.response["data"][0]["type"] == '禁止IP地址登录'

    result_delete = delet_access_audit(envi.admin, key=result_ip.response["data"][0]["key"])
    assert result_delete.success is True

    result_query = access_audit_query(envi.admin)
    assert result_query.response["data"] == []

    result_login_nomal = login_times(envi,loginName='ghca',password='111111',times=1)
    assert result_login_nomal[0].success is True

    result_login_nomal2 = login_times(envi, loginName='liulj',password='111111',times=1)
    assert result_login_nomal2[0].success is True, result_login_nomal2[0].error
if __name__ == "__main__":
    pytest.main(["-s", "test_00_login.py",'--alluredir', './temp'])
    # # os.system('allure generate ./temp -o ./report --clean')
    # Koal.web_login()
