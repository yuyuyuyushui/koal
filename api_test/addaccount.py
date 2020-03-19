from koal import *
if __name__== "__main__":
    koal = Koal("https://10.11.220.162", token='80af7b94ec9ed68d23973372fcf7a0d7')
    resid = None
    data = {
        "resId":resid,
        "type":1,
        "accountCategory": 1,
        "accountName": "root",
        # "groupId": "",
        "password": "ghcatest",
        "needDeposit":0,
        # "policyId": 4,
        # "status": 0,
        "securityLevel": 0
    }