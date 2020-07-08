from operations.organize import *
import pytest
from random import randint
from library.loggins import *
import sys

def test_delet_first_level_organaze(koal,parentid=0,first_name="delete_first_name_{}".format(randint(0,999))):
    result_lv1= add_organize_and_get_deptId(koal,parentid,first_name)
    assert result_lv1.success, result_lv1.error
