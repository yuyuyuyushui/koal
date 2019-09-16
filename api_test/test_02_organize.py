from operations.organize import *
import pytest
from random import randint
add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999)),0),
    (5,'add_organize_{}'.format(randint(1,9999)),0,)
]

@pytest.mark.parametrize("parentid, deptname,expected", add_organize_testdata)
def test_add_organize(env, parentid, deptname,expected):
    result = add_organize(env.koal, parentid, deptname)
    print(result.json())
    assert result.json()['code'] == expected
    assert result.json()['msg'] == "添加机构成功"

# def test_update_organize(env):
#     result = update_organize(env.koal)
#     assert result.json()['code'] == 0
#     assert 0
if __name__=='__main__':
    pytest.main()