def add_organize_and_get_deptId(koal, parentid, deptname):
    organize = {
        "parentId": parentid,
        "deptName": deptname
    }
    result = koal.organize_manage.add_organize(json=organize)
    if result.success == False:
        return result
    result_query = koal.organize_manage.query_organize()
    if result_query.success == False:
        return result_query
    for i in result_query.response["data"]:
        if i["deptName"] == deptname:
            result_query.deptId = i["deptId"]
    if result_query.deptId == None:
        result_query.success = False
    return result_query