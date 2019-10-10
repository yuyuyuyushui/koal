from core.base import CommonItem


def business_system_list(koal, page, limit):
    param = {
        "page": page,
        "limit": limit
    }
    result = CommonItem()
    response = koal.business_system.query_business_system_list(params=param)
    print(response.json())
    if response.json()["code"] != 0 :
        result.error = "查询失败，返回码{}".format(response.json()["code"])
        return result
    result.success = True
    result.response = response.json()
    return result