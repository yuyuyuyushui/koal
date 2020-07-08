from operations.organize import *
import pytest
from random import randint
from library.loggins import *


def test_add_fist_levels_organize_nomal(koal):
    logger_debug("测试添加一级部门")
    result = add_organize_and_get_deptId(koal, 0, 'test_add_44')
    assert result.success == True, result.error
    response_delete = delele_organize(koal, result.deptId)
    assert response_delete.success == True, response_delete.error


add_organize_testdata = [
    (0, 'add_organize_{}'.format(randint(1, 9999))),
]


@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_two_same_organize_name(koal, parentid, deptname):
    logger_debug("测试两个相同的部门名称")
    result = add_organize_and_get_deptId(koal, parentid, deptname)
    assert result.success == True, result.error
    dept_response_same = add_organize_and_get_deptId(koal, parentid, deptname)
    assert dept_response_same.success == False
    assert dept_response_same.response["msg"] == '添加机构失败. 机构重名.'
    response_delete = delele_organize(koal, result.deptId)
    assert response_delete.success == True, response_delete.error


def test_add_two_levels_organize_name(koal, parentid=0, deptname='add_two_levels_{}'.format(randint(1, 999))):
    logger_debug("测试添加两级部门，部门名称相同")
    result_first_lv1 = add_organize_and_get_deptId(koal, parentid, deptname)
    assert result_first_lv1.success == True, result_first_lv1.error
    response_two_level = add_organize_and_get_deptId(koal, deptname=deptname, parentid=result_first_lv1.deptId)
    assert response_two_level.success == True, response_two_level.error

    response_delete = delele_organize(koal, result_first_lv1.deptId)
    assert response_delete.success == True, response_delete.error


def test_add_two_levels_organize_name_diff(koal, parentid=0, deptname='fist_levels_{}'.format(randint(1, 999)),
                                           two_levle_deptname='second_levels_{}'.format(randint(1, 999))):
    logger_debug("测试添加两级部门，部门名称不同")
    response_lv1 = add_organize_and_get_deptId(koal, parentid, deptname)
    assert response_lv1.success == True, response_lv1.error
    response_lv2 = add_organize_and_get_deptId(koal, deptname=two_levle_deptname, parentid=response_lv1.deptId)
    assert response_lv2.success == True, response_lv2.error
    delete_orgs(koal, [response_lv2.deptId, response_lv1.deptId])


def test_add_two_levels_organize_name_double_same_subsidiary_name(koal, parentid=0,
                                                                  deptname='fist_levels_{}'.format(randint(1, 999)),
                                                                  two_levle_deptname='second_levels_{}'.format(
                                                                      randint(1, 999))):
    logger_debug("测试添加两级部门两个子部门，子部门名称相同")
    result_lv1= add_organize_and_get_deptId(koal, parentid, deptname)
    assert result_lv1.success == True, result_lv1.error
    result_lv2 = add_organize_and_get_deptId(koal, deptname=two_levle_deptname,parentid=result_lv1.deptId)
    assert result_lv2.success == True, result_lv2.error
    result_lv2_1 = add_organize_and_get_deptId(koal, deptname=two_levle_deptname,
                                                                       parentid=result_lv1.deptId)
    assert result_lv2_1.success == False, result_lv2_1.error
    delete_orgs(koal,[result_lv2.deptId, result_lv1.deptId])


def test_add_two_levels_organize_name_double_diff_subsidiary_name(koal, parentid=0,
                                                                  deptname='fist_levels_{}'.format(randint(1, 999)),
                                                                  two_levle_deptname='second_levels_{}'.format(
                                                                      randint(1, 999)),
                                                                  two_levle_second_deptname='second_levels_{}'.format(
                                                                      randint(1, 999))):
    logger_debug('测试添加两级部门，两级子部门名称不同')
    result_lv1 = add_organize_and_get_deptId(koal, parentid, deptname)
    assert result_lv1.success is True, result_lv1.error
    result_lv2_1 = add_organize_and_get_deptId(koal, deptname=two_levle_deptname, parentid=result_lv1.deptId)
    assert result_lv2_1.success is True, result_lv2_1.error
    result_lv2_2 = add_organize_and_get_deptId(koal, parentid=result_lv1.deptId, deptname=two_levle_second_deptname)
    assert result_lv2_2.success is True, result_lv2_2.error
    delete_orgs(koal, [result_lv2_2.deptId, result_lv2_1.deptId, result_lv1.deptId])


if __name__ == '__main__':
    pytest.main(['-s', "test_01_organize_add.py"])
