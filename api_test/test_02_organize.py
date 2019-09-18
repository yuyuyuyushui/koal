from operations.organize import *
import pytest
from random import randint
add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999))),
    (5,'add_organize_{}'.format(randint(1,9999)))
]

@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_organize(env, parentid, deptname):
    result = add_organize(env.koal, parentid, deptname)
    print(result)
    assert result.success == True, result.error

def test_delete_organize(env):
    pass
data_param = {
    (1,10,None)
}
@pytest.mark.parametrize("page,limit,param",data_param)
def test_query_organize(env,page,limit,param):
    """
    查询组织结构系统
    :param env:
    :param page:
    :param limit:
    :param param:
    :return:
    """
    result = query_organize(env.koal,page,limit,param)
    assert result.json()["code"] == 0

if __name__=='__main__':
    pytest.main("-V -s test_02_organize.py")