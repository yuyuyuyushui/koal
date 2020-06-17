from core.base import *


class Business_system_api():
    def __init__(self, koal):
        self.koal = koal

    def business_system_list(self,page, limit):
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
        return self.koal.business_system.query_business_system_list(params=param)

    def delet_busuness_system(self, abisid):
        """
        根据业务系统id删除业务系统
        :param abisid:
        :return:
        """
        return self.koal.business_system.delete_business_system(abisid)

    def add_business_system(self, abisname, workflownodenum, abisadminids):
        """
        新增业务系统
        :param abisname:
        :param workflownodenum: 临时收取审批节点数
        :param abisadminids: 管理员id
        :return:
        """
        add_data={
            "abisName":abisname,
            "workflowNodeNum":workflownodenum,
            "abisAdminIds":abisadminids
        }
        logger_info(add_data)
        return self.koal.business_system.add_business_system(json=add_data)

    def query_business_detail(self, abisid):
        """
        查询业务系统详情
        :param abisid:
        :return:
        """
        return self.koal.business_system.query_business_detail(abisid)

    def modify_business_system(self, abisId, abisName, workflowNodeNum, abisAdminIds):
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
            "abisAdminIds":"abisAdminIds"
        }
        return self.koal.business_system.modify_business_system(abisId,json=json_data)

    def query_business_admin_list(self, abisid):
        """
        查询业务系统管理员列表
        :param abisid:业务系统id
        :return:
        """
        return self.koal.business_system.query_business_admin_list(abisid)

    def modify_business_admin_jurisdiction(self, id, permsSetPassword, permsViewPassword, permsApproveFirst, permsApproveSecond, receiveWarn):
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
        return self.koal.business_system.modify_business_admin_jurisdiction(json=admin_data)

    def query_admin(self, keyword, page, limit, abisId=None):
        """
        检索待添加的管理员
        :param keyword:查询条件
        :param page:当前页
        :param limit:页大小
        :param abisId:
        :return:
        """
        query_data={
            "keyword":keyword,
            "page":page,
            "limit":limit,
            "abisId":abisId
        }
        return self.koal.business_system.query_admin(params=query_data)
def query_business_system_list(koal,page, limit):
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


def add_business_system(koal,abisname, workflownodenum, abisadminids ):
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
def query_busuness_system_list(koal,page,limit):
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

def query_admin_list(koal,keyword, page, limit, abisId=None):
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
    response = query_admin_list(koal,keyword, page, limit, abisId)
    if response.success == False:
        return response
    for i in response.response["page"]["list"]:
        userid = userid + i["userId"] + ","
    return add_business_system(koal, abisname, workflownodenum, userid)


def query_admin_list_and_add_business_system_delete(koal, keyword, page, limit, abisname, workflownodenum,  abisId=None):
    response = query_admin_list_and_add_business_system(koal, keyword, page, limit, abisname, workflownodenum,  abisId=None)
    if response.success ==False:
        return response
    response_system_list=query_business_system_list(koal,page, limit)
    if response_system_list==False:
        return response
    # abisId=None
    print(response_system_list)
    for i in response_system_list.response["page"]["list"]:
        print(i)
        if abisname == i["abisName"]:
            abisid = i["abisId"]
            print(abisid)
    print(abisId)
    return delete_business_system(koal,abisid)


