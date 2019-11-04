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
        param = {
            "page": page,
            "limit": limit,
            "resKind": resKind,
            "abisId": abisId
        }
        return self.koal.it_assert.assert_list(params=param)
    def add_assert(self, resName):
