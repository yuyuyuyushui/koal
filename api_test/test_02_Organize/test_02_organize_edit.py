from operations.organize import *
import pytest
from random import randint
from library.loggins import *
import sys

def test_edit_organize_nomal(koal,parentid=0,dept_old_name='test_edit_{}'.format(randint(1,999)),dept_new_Name='test_edit_new_{}'.format(randint(1,999)),):

    logger_info('测试编辑部门')
    # dept_response = add_organize_and_get_deptId(koal,parentid,dept_old_name)
    # assert dept_response.success==True, dept_response.error
    # assert dept_response.deptId != None
    # deptId = dept_response.deptId
    # edit_response = edit_organize(koal,deptId,dept_new_Name,parentid)
    # assert edit_response.success==True,edit_response.error
    # assert edit_response.response['msg'] == '修改机构成功'
    # delete_response= delele_organize(koal,deptId)
    # assert delete_response.success==True, delete_response.error


if __name__=='__main__':
    pytest.main(['-s', "test_02_organize_edit.py::test_edit_organize"])