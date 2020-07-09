

def access_audit_query(koal):
    '''
    关键字:访问审计查询
    :param koal:
    :return:{'msg': '成功', 'code': 0, 'data': []}
    [{"key":"login:fail:forbidden:10.1.6.81","type":"禁止IP地址登录","remark":"10.1.6.81","forbiddenTime":"2020-07-09 13:30:11"},{"key":"login:fail:user:forbidden:ghca:","type":"禁止用户登录","remark":"ghca","forbiddenTime":"2020-07-09 13:29:50"}]
    '''
    # param ={
    #     't':1594262046063
    # }
    result = koal.access_audit.access_isolation()
    return result

def delet_access_audit(koal,key):
    """
    关键字：删除访问隔离
    :param koal:
    :param key:
    :return:
    """
    data={
        'key':key
    }
    return koal.access_audit.delete_isolation(json=data)
