class Asseart_account():
    def __init__(self, koal):
        self.koal = koal

    def accunt_list_export(self, abisId, resId):
        param = {
            "abisId": abisId,
            "resId": resId
        }
        return self.koal.assert_accunt_manage.accunt_list_export(params=param)