class Asseart_account():
    def __init__(self, koal):
        self.koal = koal

    def accunt_list_export(self,abisId, resId):
        """
        账号列表导出
        :param abisId: 业务系统ID
        :param resId: 资源ID
        :return:
        """
        param = {
            "abisId": abisId,
            "resId": resId
        }
        return self.koal.assert_accunt_manage.accunt_list_export(params=param)
