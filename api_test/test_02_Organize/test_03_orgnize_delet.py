from operations.organize import *
import pytest
from random import randint
from library.loggins import *
import sys

data=[
    ('admin',0, ranint_name('test'),True),
    ('ghcatest',0, ranint_name('test'),True),
    ('ghca',0, ranint_name('test'),True)
]


@pytest.mark.parametrize('role,parentid,first_name,expect',data)
def test_delet_first_level_organaze(envi, role, parentid, first_name, expect):
    koalAdmin = getattr(envi,role)
    result_lv1= add_organize_and_get_deptId(koalAdmin, parentid, first_name)
    assert result_lv1.success == expect, result_lv1.error


if __name__ == '__main__':
    pytest.main(['-s', "test_03_orgnize_delet.py"])