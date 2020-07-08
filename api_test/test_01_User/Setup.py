import pytest
from operations.organize import *
from operations.roles import *

role_organize_date=[
    ('0',"test1",None,1,"安全管理员",'系统所有权限',1,100),
    ('0',"test2",None,1,"系统管理员",'系统所有权限',1,100)
]

@pytest.mark.parametrize("parentid,deptname,identity, parentId, rolename, remark, page, limit",role_organize_date)
@pytest.fixture(scope=function)
def Role_Organize_Date(koal,parentid,deptname,identity, parentId, rolename, remark, page, limit):
    """
    测试之前添加部门和角色
    :param koal:
    :param parentid:
    :param deptname:
    :param identity:
    :param parentId:
    :param rolename:
    :param remark:
    :return:
    """
    try:
        response_query_dept = query_organize(koal)
        if response_query_dept.success ==False:
            raise Exception("查询组织机构失败")
        for i in response_query_dept.response["data"]:
            if deptname == i["deptName"]:
                raise Exception("部门已存在")
        query_roles_response = query_roles(koal, page, limit, param=None)
        if query_roles_response.success ==False:
            raise Exception("查询角色失败")
        for i in query_roles_response.response["page"]["list"]:
            if i["roleName"] == rolename:
                raise Exception("角色已添加")
    except Exception as e:
        print(e)
    add_organize_and_get_deptId(koal, parentid, deptname)
    add_role(koal,identity, parentId, rolename, remark)
