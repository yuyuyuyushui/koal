from core.base import *

class Business_system_api():
    def __init__(self, koal):
        self.koal = koal

    def business_system_list(self,page, limit):
        param = {
            "page": page,
            "limit": limit
        }
        return self.koal.business_system.query_business_system_list(params=param)

    def delet_busuness_system(self, abisid):
        return self.koal.business_system.delete_business_system(abisid)

    def add_business_system(self, abisname, workflownodenum,abisadminids):
        add_data={
            "abisName":abisname,
            "workflowNodeNum":workflownodenum,
            "abisAdminIds":abisadminids
        }
        return self.koal.business_system.add_business_system(json=add_data)

    def query_business_detail(self,abisid):
        return self.koal.business_system.query_business_detail(abisid)


    def query_business_admin_list(self, abisid):
        return  self.koal.business_system.query_business_system_list(abisid)

    def modify_business_admin_jurisdiction(self, id, permsSetPassword, permsViewPassword,permsApproveFirst,permsApproveSecond, receiveWarn):
        admin_date = {
            "id":id,
            "permsSetPassword":permsSetPassword,
            "permsViewPassword":permsViewPassword,
            "permsApproveFirst":permsApproveFirst,
            "permsApproveSecond":permsApproveSecond,
            "receiveWarn":receiveWarn
        }
        return self.koal.business_system.modify_business_admin_jurisdiction(json=admin_date)

    def query_admin(self,keyword, page, limit, abisId=None):
        query_data={
            "keyword":keyword,
            "page":page,
            "limit":limit,
            "abisId":abisId
        }
        return self.koal.business_system.query_admin(params=query_data)