from operations.organize import *
import pytest
from random import randint
# def test_add_organize(env):
#     result = add_organize(env.koal, 0, 'test_add_{}'.format(randint(0,9999)))
#     print(result.json())
#     assert result.json()['code'] == 0
#     assert result.json()['msg'] == "添加机构成功"

def test_update_organize(env):
    result = update_organize(env.koal)
    assert result.json()['code'] == 0
    assert 0
if __name__=='__main__':
    pytest.main()