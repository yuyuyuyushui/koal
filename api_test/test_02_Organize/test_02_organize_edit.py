from operations.organize import *
import pytest
from random import randint
from library.loggins import *
import sys

def test_edit_first_level_organize_nomal(koal,parentid=0,dept_old_name='test_edit_{}'.format(randint(1,999)),dept_new_Name='test_edit_new_{}'.format(randint(1,999)),):
    logger_info('测试编辑部门')
    result_lv1 = add_organize_and_get_deptId(koal, parentid, dept_old_name)
    assert result_lv1.success==True, result_lv1.error
    edit_response = edit_organize(koal,result_lv1.deptId, dept_new_Name, parentid)
    assert edit_response.success==True,edit_response.error
    assert edit_response.response['msg'] == '修改机构成功'
    delete_response= delele_organize(koal,result_lv1.deptId)
    assert delete_response.success==True, delete_response.error


def test_edit_second_levle_org_name(koal, parentid=0, dept_first_name='first_dept_name{}'.format(randint(0,999)),dept_second_name='second_name_{}'.format(randint(1,999)),dept_second_edit_name="second_edit_name{}".format(randint(0,999))):
    logger_debug('编辑二级部门名称')
    result_lv1 = add_organize_and_get_deptId(koal, parentid, dept_first_name)
    assert result_lv1.success == True, result_lv1.error
    result_lv2 = add_organize_and_get_deptId(koal,result_lv1.deptId,dept_second_name)
    assert result_lv2.success is True, result_lv2.error
    result_lv2_edit = edit_organize(koal,result_lv2.deptId,dept_second_edit_name,result_lv1.deptId)
    assert result_lv2_edit.success, result_lv2_edit.error
    delete_orgs(koal,[result_lv2.deptId,result_lv1.deptId])


if __name__=='__main__':
    pytest.main(['-s', "test_02_organize_edit.py::test_edit_second_levle_org_name"])