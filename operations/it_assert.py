class It_assert():
    def __init__(self, koal):
        self.koal = koal

    def dictionary_data_query(self,type, tag):
        param = {
            "type": type,
            "tag": tag
        }
        return self.koal.it_assert.dictionary_data(params=param)

    def business_system_query(self):
        return self.koal.it_assert.business_system()

    def assert_list_query(self, page, limit, resKind, abisId):
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
        return self.koal.it_assert.assert_list(params=param)

    def add_assert(self, resName, abisId, resKind, resCategory, ip4Addr, resVersion, resType, cmdPrompt, protocolPort, winDomain,instanceName, databaseName, httpLoginUri, status, asJumpDevice, needJumpLogin, fromResId, fromAccountId, fromCommand, ip_white):
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
        return self.koal.it_assert.add_assert(json=json_data)

    def modify_assert(self, resId, resName,abisId, resKind, resCategory, ip4Addr, resVersion, resType, cmdPrompt, protocolPort, winDomain,instanceName, databaseName, httpLoginUri, status, asJumpDevice, needJumpLogin, fromResId, fromAccountId, fromCommand, ip_white):
        """
        修改资产
        :param resId: 资源id
        :param resName:
        :param resKind:
        :param resCategory:
        :param ip4Addr:
        :param resVersion:
        :param resType:
        :param cmdPrompt:
        :param protocolPort:
        :param winDomain:
        :param instanceName:
        :param databaseName:
        :param httpLoginUri:
        :param status:
        :param asJumpDevice:
        :param needJumpLogin:
        :param fromResId:
        :param fromAccountId:
        :param fromCommand:
        :param ip_white:
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
        return self.koal.it_assert.modify_assert(json=json_date)

    def delete_assert(self, resId):
        """
        删除资产
        :param resId:
        :return:
        """
        return self.koal.it_assert.delete_assert(resId)

    def assert_accunt_find(self):
        """
        资产账号发现
        :return:
        """
        return self.koal.it_assert.assert_accunt_query()

    def query_assert_detail(self, resId):
        """
        查看资源详情
        :return:
        """
        return self.koal.it_assert.query_assert_detail(resId)