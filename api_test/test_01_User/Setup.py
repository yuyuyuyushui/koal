import pytest
from operations.organize import *
from operations.roles import *

@pytest.fixture(scope=function)
def Role_Organize(env):
    add_organize(env.koal,1,'add-user')
    add_role(env.koal,'add-user-role','333')
