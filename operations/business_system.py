from core.base import *


def query_business_system_list(koal, page, limit):
    """
            分页查询业务系统列表
            :param page:
            :param limit:
            :return:
            """
    param = {
        "page": page,
        "limit": limit
    }
    return koal.business_system.query_business_system_list(params=param)


def add_business_system(koal,abisname, workflownodenum, abisadminids):
    """
    添加业务系统
    :param koal:
    :param abisname:
    :param workflownodenum:
    :param abisadminids:
    :return:
    """
    add_data = {
        "abisName": abisname,
        "workflowNodeNum": workflownodenum,
        "abisAdminIds": abisadminids
    }
    logger_info(add_data)
    return koal.business_system.add_business_system(json=add_data)


def delete_business_system(koal,abisid):
    """
    删除业务系统
    :param koal: 登录token
    :param abisid: 业务id
    :return:
    """
    return koal.business_system.delete_business_system(abisid)





def modify_business_system(koal,abisId, abisName, workflowNodeNum, abisAdminIds):
    """
    修改业务系统
    :param abisId: 业务系统id
    :param abisName: 业务系统名
    :param workflowNodeNum: 临时收取审批节点数
    :param abisAdminIds:管理员IDS(多个)
    :return:
    """
    json_data={
        "abisName":abisName,
        "workflowNodeNum":workflowNodeNum,
        "abisAdminIds":abisAdminIds
    }
    return koal.business_system.modify_business_system(abisId,json=json_data)


def query_system_admin_list(koal, keyword, page, limit, abisId=None):
    """
        检索待添加的管理员
        :param keyword:查询条件
        :param page:当前页
        :param limit:页大小
        :param abisId:
        :return:
    """
    query_data = {
        "keyword": keyword,
        "page": page,
        "limit": limit,
        "abisId": abisId
    }
    return koal.business_system.query_admin(params=query_data)




def modify_business_admin_jurisdiction(koal, id, permsSetPassword, permsViewPassword, permsApproveFirst, permsApproveSecond, receiveWarn):
    """
    修改业务系统管理员权限
    :param id:
    :param permsSetPassword:重置密码权限
    :param permsViewPassword:查看密码权限
    :param permsApproveFirst:审核节点1权限
    :param permsApproveSecond:审核节点2权限
    :param receiveWarn:是否接收资源告警
    :return:
    """
    admin_data = {"adminList" :[{
        "id":id,
        "permsSetPassword":permsSetPassword,
        "permsViewPassword":permsViewPassword,
        "permsApproveFirst":permsApproveFirst,
        "permsApproveSecond":permsApproveSecond,
        "receiveWarn":receiveWarn
    }]}
    return koal.business_system.modify_business_admin_jurisdiction(json=admin_data)

def admin_jursisdiction_set(koal,abisId):
    """
    根据业务系统ID，查询业务系统管理员权限设置
    :param koal:
    :param abisId:
    :return:
    """
    return koal.business_system.admin_jursisdiction_set(abisId)

def query_business_system_detail(koal,abisid):
    """
       查询业务系统详情权限
        :param abisid:
         :return:
    """
    return koal.business_system.query_business_detail(abisid)


def username_and_query_userId(koal,loginname):
    """
    根据用户名查询用户Id
    :param koal:
    :param loginname:
    :return:
    """
    result_query = query_system_admin_list(koal,keyword=loginname,page=1,limit=100)
    if result_query.success is False:
        return result_query
    if loginname in result_query.response["page"]["list"][0]["loginName"]:
        result_query.userId = result_query.response["page"]["list"][0]["userId"]
    return result_query


def query_admin_list_and_get_amdin_id(koal, keyword, page, limit, abisId=None):
    """
         查询管理员列表，获取管理员ID
        :param keyword:查询条件
        :param page:当前页
        :param limit:页大小
        :param abisId:业务系统ID
        :return:
    """
    query_data = {
        "keyword": keyword,
        "page": page,
        "limit": limit,
        "abisId": abisId
    }
    response = koal.business_system.query_admin(params=query_data)
    if response==False:
        return response
    userid = ''
    for i in response.response["page"]["list"]:
        userid = userid + i["userId"] + ","
    response.userid=userid.strip(',')
    return response



def query_business_list_and_get_business_id(koal,page, limit,abisname):
    """
    查询业务系统列表获取业务系统id
    :param koal:
    :param page:
    :param limit:
    :param abisname:
    :return:
    """
    response = query_business_system_list(koal,page,limit)
    if response.success == False:
        return response
    for i in response.response["page"]["list"]:
        if abisname==i["abisName"]:
            response.abisname=abisname
            response.abisId = i["abisId"]
    return response


def query_admin_list_and_get_admin_id(koal, keyword, page, limit, userName):
    response = query_system_admin_list(koal, keyword, page, limit, abisId=None)
    if response.success==False:
        return response
    for i in response.response["page"]["list"]:
        if userName == i["loginName"]:
            response.userId = i["userId"]
    return response


def query_admin_list_and_add_business_system(koal, keyword, page, limit, abisname, workflownodenum,  abisId=None):
    """
    查询管理员列表并获取管理员id，再添加业务系统
    :param koal:
    :param keyword:管理员关键字
    :param page:页码
    :param limit:个数
    :param abisname:业务系统名称
    :param workflownodenum:工作节点
    :param abisId:管理员id
    :return:
    """
    userid= ''
    response = query_system_admin_list(koal,keyword, page, limit, abisId)
    if response.success == False:
        return response
    for i in response.response["page"]["list"]:
        userid = userid + i["userId"] + ","
    return add_business_system(koal, abisname, workflownodenum, userid)




