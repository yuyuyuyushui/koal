from core.base import CommonItem
def response(func):
    def wrapper(*args, **kwargs):
        result = CommonItem()
        response = func(*args, **kwargs)
        if response.json() != 0:
            result.error = "的返回码{}".format(response.json()["code"])
            result.response=response.json()
        result.success = True
        result.response = response.json()
        return result
    return wrapper
@response
def business_system_list(koal, page, limit):
    param = {
        "page": page,
        "limit": limit
    }
    return koal.business_system.query_business_system_list(params=param)


def add_business_system(koal, abisname, workflownodenum,abisadminids):
    add_data={
        "abisName":abisname,
        "workflowNodeNum":workflownodenum,
        "abisAdminIds":abisadminids
    }
    result = CommonItem()
    response = koal.business_system.add_business_system(json=add_data)
    if response.json()["code"] != 0:
        result.error="新增业务系统失败，返回码{}".format(response.json()["code"])
        return result
    result.success=True
    result.response = response.json()
    return result
# @response
def delet_busuness_system(koal, abisid):
    response = koal.business_system.delete_business_system(abisid)
    result = CommonItem()

    if response.json() != 0:
        result.error = "的返回码{}".format(response.json()["code"])
        result.response = response.json()
    result.success = True
    result.response = response.json()
    return result