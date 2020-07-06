from operations.organize import *
import pytest
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

def test_add_two_levels_organize_name(koal, parentid=0, deptname='add_two_levels_{}'.format(randint(1,999))):
    response_add=add_organize(koal, parentid, deptname)
    assert response_add.success==True, response_add.error
    response_dept_id = dept_name_and_get_deptId(koal,deptname)
    assert response_dept_id.success==True, response_dept_id.error
    response_two_level = add_organize(koal,deptname=deptname,parentid=response_dept_id.deptId)
    assert response_two_level.success==True, response_dept_id.error
if __name__=='__main__':
    pytest.main(['-s', "test_01_organize_add.py::test_add_two_levels_organize_name"])