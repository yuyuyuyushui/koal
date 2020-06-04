from operations.organize import *
import pytest
from random import randint
add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999))),
    # (5,'add_organize_{}'.format(randint(1,9999)))
]


@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_organize(env, parentid, deptname):
    result = add_organize(env.koal, parentid, deptname)
    # print(result)
    # assert result.success == True, result.error
    pytest.assume(result.response["msg"] == "添加机构成功1")
    pytest.assume(result.response["code"] == 0)

def test_delete_organize(env):
    pass


def test_qury_orgize(env):
    response = query_organize(env.koal)
    print(response.response)
    # pytest.assume(response.success==True)
    # pytest.assume(response.response['msg'] == 3)
    assert 0


if __name__=='__main__':
    pytest.main(['-s', "test_02_organize.py::test_add_organize"])