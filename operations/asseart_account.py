class Asseart_account():
    def __init__(self, koal):
        self.koal = koal

    def accunt_list_export(self,abisId, resId):
        """
        �˺��б���
        :param abisId: ҵ��ϵͳID
        :param resId: ��ԴID
        :return:
        """
        param = {
            "abisId": abisId,
            "resId": resId
        }
        return self.koal.assert_accunt_manage.accunt_list_export(params=param)
