from operations.business_system import *
import pytest

business_data=[
    (1, 10),
    (1, 25),
    (1, 50)
]
@pytest.mark.parametrize("page,limit",business_data)
def test_business_system(env,page,limit):
    resonse = business_system_list(env.koal, page, limit)
    assert resonse.success == True, resonse.error
    assert 0
if __name__=="__main__":
    pytest.main(["-s","test_04_businuess_system::test_business_system"])