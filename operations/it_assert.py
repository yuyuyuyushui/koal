
def dictionary_data_query(koal,type, tag):
    param = {
        "type": type,
        "tag": tag
    }
    return koal.it_assert.dictionary_data(params=param)


def business_system_query(koal):
    """
    业务系统查询
    :param koal:
    :return:
    """
    return koal.it_assert.business_system()

def assert_list_query(koal, page, limit, resKind, abisId):
    """
    资产列表查询
    :param page:
    :param limit:
    :param resKind:
    :param abisId:
    :return:
    """
    param = {
        "page": page,
        "limit": limit,
        "resKind": resKind,
        "abisId": abisId
    }
    return koal.it_assert.assert_list(params=param)

def add_assert(koal, resName, abisId, resKind, resCategory, ip4Addr, resVersion, resType, protocolPort ,ip_white, status, cmdPrompt=None, winDomain=None,instanceName=None, databaseName=None, httpLoginUri=None, asJumpDevice=None, needJumpLogin=None, fromResId=None, fromAccountId=None, fromCommand=None):
        """
        添加资产
        :param resName: 资源名称
        :param abisId: 所属业务系统ID
        :param resKind: 资产类别
        :param resCategory: 设备类型
        :param ip4Addr: IP地址
        :param resVersion: 系统版本
        :param resType: 系统类型
        :param cmdPrompt: 命令提示符
        :param protocolPort:协议端口
        :param winDomain:归属windows域
        :param instanceName:数据库实例
        :param databaseName:数据库名称
        :param httpLoginUri:应用资源登录uri
        :param status:状态
        :param asJumpDevice:是跳转设备
        :param needJumpLogin:是否跳转才能登录
        :param fromResId:跳转设备ID
        :param fromAccountId:跳转账号
        :param fromCommand:跳转命令
        :param ip_white:允许访问ip白名单
        :return:
        """
        json_data = {
            "resName":resName,
            "abisId":abisId,
            "resKind":resKind,
            "resCategory":resCategory,
            "ip4Addr": ip4Addr,
            "resVersion": resVersion,
            "resType": resType,
            "cmdPrompt":cmdPrompt,
            "protocolPort": protocolPort,
            "winDomain":winDomain,
            "instanceName":instanceName,
            "databaseName":databaseName,
            "httpLoginUri":httpLoginUri,
            "status":status,
            "asJumpDevice":asJumpDevice,
            "needJumpLogin":needJumpLogin,
            "fromResId":fromResId,
            "fromAccountId":fromAccountId,
            "fromCommand":fromCommand,
            "ip_white":ip_white
        }
        return koal.it_assert.add_assert(json=json_data)
def modify_assert(koal, resId, resName, abisId, resKind, resCategory, ip4Addr, resVersion, resType,protocolPort ,ip_white, status, cmdPrompt=None, winDomain=None,instanceName=None, databaseName=None, httpLoginUri=None, asJumpDevice=None, needJumpLogin=None, fromResId=None, fromAccountId=None, fromCommand=None):
    """
    修改资产
    :param resId:
    :param resName:
    :param abisId:
    :param resKind:
    :param resCategory:
    :param ip4Addr:
    :param resVersion:
    :param resType:
    :param protocolPort:
    :param ip_white:
    :param status:
    :param cmdPrompt:
    :param winDomain:
    :param instanceName:
    :param databaseName:
    :param httpLoginUri:
    :param asJumpDevice:
    :param needJumpLogin:
    :param fromResId:
    :param fromAccountId:
    :param fromCommand:
    :return:
    """
    json_date={
        "resId": resId,
        "resName": resName,
        "abisId": abisId,
        "resKind": resKind,
        "resCategory": resCategory,
        "ip4Addr": ip4Addr,
        "resVersion": resVersion,
        "resType": resType,
        "cmdPrompt": cmdPrompt,
        "protocolPort": protocolPort,
        "winDomain": winDomain,
        "instanceName": instanceName,
        "databaseName": databaseName,
        "httpLoginUri": httpLoginUri,
        "status": status,
        "asJumpDevice": asJumpDevice,
        "needJumpLogin": needJumpLogin,
        "fromResId": fromResId,
        "fromAccountId": fromAccountId,
        "fromCommand": fromCommand,
        "ip_white": ip_white
    }
    return koal.it_assert.modify_assert(json=json_date)
def delete_assert(koal, resId):
    """
    根据资产Id删除资产
    :param resId:
    :return:
    """
    return koal.it_assert.delete_assert(resId)

def assert_accunt_find(koal):
    """
    资产账号发现
    :return:
    """
    return koal.it_assert.assert_accunt_query()

def query_assert_detail(koal, resId):
    """
    根据资源ID查看资源详情
    :return:
    """
    return koal.it_assert.query_assert_detail(resId)