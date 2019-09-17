from operations.organize import *
import pytest
from random import randint
add_organize_testdata=[
    (0,'add_organize_{}'.format(randint(1,9999))),
    (5,'add_organize_{}'.format(randint(1,9999)))
]

@pytest.mark.parametrize("parentid, deptname", add_organize_testdata)
def test_add_organize(env, parentid, deptname):
    result = add_organize(env.koal, parentid, deptname)
    print(result)
    assert result.success == True, result.error

# def test_query_organize(env):
#     result = query_organize(env.koal)
#     print(result.json())

if __name__=='__main__':
    pytest.main()