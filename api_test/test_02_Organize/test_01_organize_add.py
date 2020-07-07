from operations.organize import *
import pytest
from random import randint
from library.loggins import *


def test_add_fist_levels_organize_nomal(koal):
    logger_debug("测试添加一级部门")
    result = add_organize(koal, 0, 'test_add_44')
    assert result.success == True, result.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, 'test_add_44')
    assert response_dept_id.success==True,response_dept_id.error
    response_delete = delele_organize(koal,response_dept_id.deptId)
    assert response_delete.success==True,response_delete.error


add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999))),
]

@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_two_same_organize_name(koal,parentid,deptname):
    logger_debug("测试两个相同的部门名称")
    dept_response = add_organize(koal,parentid,deptname)
    assert dept_response.success==True, dept_response.error
    dept_response_same = add_organize(koal,parentid,deptname)
    assert dept_response_same.success== False
    assert dept_response_same.response["msg"] == '添加机构失败. 机构重名.'
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success == True, response_dept_id.error
    response_delete = delele_organize(koal, response_dept_id.deptId)
    assert response_delete.success == True, response_delete.error


def test_add_two_levels_organize_name(koal, parentid=0, deptname='add_two_levels_{}'.format(randint(1,999))):
    logger_debug("测试添加两级部门，部门名称相同")
    response_add=add_organize(koal, parentid, deptname)
    assert response_add.success==True, response_add.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success==True, response_dept_id.error
    response_two_level = add_organize(koal,deptname=deptname,parentid=response_dept_id.deptId)
    assert response_two_level.success==True, response_dept_id.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success == True, response_dept_id.error
    # response_delete = delele_organize(koal, response_dept_id.deptId)
    #     # assert response_delete.success == True, response_delete.error

def test_add_two_levels_organize_name_diff(koal, parentid=0, deptname='fist_levels_{}'.format(randint(1,999)),two_levle_deptname='second_levels_{}'.format(randint(1,999))):
    logger_debug("测试添加两级部门，部门名称不同")
    response_add = add_organize(koal, parentid, deptname)
    assert response_add.success == True, response_add.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success == True, response_dept_id.error
    response_two_level = add_organize(koal, deptname=two_levle_deptname, parentid=response_dept_id.deptId)
    assert response_two_level.success==True,response_two_level.error
    response_second_levels = second_levels_name_and_get_deptID(koal,two_levle_deptname)
    assert response_second_levels.success == True,response_second_levels.error
    response_delete = delele_organize(koal,response_second_levels.deptId)
    assert response_delete.success==True, response_delete.error
    response_delete_first_level = delele_organize(koal,response_dept_id.deptId)
    assert response_delete_first_level.success==True,response_delete_first_level.error



def test_add_two_levels_organize_name_double_same_subsidiary_name(koal,parentid=0,deptname='fist_levels_{}'.format(randint(1,999)),two_levle_deptname='second_levels_{}'.format(randint(1,999))):
    logger_debug("测试添加两级部门两个子部门，子部门名称相同")
    response_add = add_organize(koal, parentid, deptname)
    assert response_add.success == True, response_add.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success == True, response_dept_id.error
    response_two_level_subsidiary = add_organize(koal, deptname=two_levle_deptname, parentid=response_dept_id.deptId)
    assert response_two_level_subsidiary.success==True,response_two_level_subsidiary.error
    response_two_level_subsidiary_second = add_organize(koal, deptname=two_levle_deptname, parentid=response_dept_id.deptId)
    assert response_two_level_subsidiary_second.success==False, response_two_level_subsidiary_second.error


def test_add_two_levels_organize_name_double_diff_subsidiary_name(koal,parentid=0,deptname='fist_levels_{}'.format(randint(1,999)),two_levle_deptname='second_levels_{}'.format(randint(1,999)), two_levle_second_deptname='second_levels_{}'.format(randint(1,999))):
    logger_debug('测试添加两级部门，两级子部门名称不同')
    response_add = add_organize(koal, parentid, deptname)
    assert response_add.success == True, response_add.error
    response_dept_id = first_level_dept_name_and_get_deptId(koal, deptname)
    assert response_dept_id.success == True, response_dept_id.error
    response_two_level_subsidiary = add_organize(koal, deptname=two_levle_deptname, parentid=response_dept_id.deptId)
    assert response_two_level_subsidiary.success == True, response_two_level_subsidiary.error
    response_two_level_sencond_subsidiary=add_organize(koal,parentid=response_dept_id.deptId,deptname=two_levle_second_deptname)
    assert response_two_level_sencond_subsidiary.success==True,response_two_level_sencond_subsidiary.error
if __name__=='__main__':
    pytest.main(['-s', "test_01_organize_add.py"])