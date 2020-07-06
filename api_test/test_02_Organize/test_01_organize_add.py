from operations.organize import *
import pytest,pytest_assume
from random import randint

def test_add_organize_nomal(koal):
    result = add_organize(koal, 0, 'test_add_44')
    assert result.success == True, result.error



add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999))),
]

@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_two_same_organize_name(koal,parentid,deptname):
    dept_response = add_organize(koal,parentid,deptname)
    assert dept_response.success==True, dept_response.error
    dept_response_same = add_organize(koal,parentid,deptname)
    assert dept_response_same.success== False
    assert dept_response_same.response["msg"] == '添加机构失败. 机构重名.'



if __name__=='__main__':
    pytest.main(['-s', "test_01_organize_add.py::test_add_two_same_organize_name"])