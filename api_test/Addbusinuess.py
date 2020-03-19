from api.business_system_management import *
from koal import *



if __name__== "__main__":
    import json
    koal = Koal("https://10.11.220.162", token='80af7b94ec9ed68d23973372fcf7a0d7')
    resName = 1
    # for resName in range(110,140):
    #
    #     businesdata = {
    #         "resName": "10.11.220.{}".format(resName),
    #         "abisId": "361d045120c809d2ce4df3950390962e",
    #         "resKind": 1,
    #         "resCategory": 1,
    #         "ip4Addr": "10.11.220.{}".format(resName),
    #         "protocolPortList": json.dumps([{"protocols": "ssh", "port": 22, "established": "true"}, {"protocols": "sftp", "port": 22, "established": "true"}])}
    #

    businesdata = {
        "resName": "10.11.220.{}".format(resName),
        "abisId": "361d045120c809d2ce4df3950390962e",
        "resKind": 1,
        "resCategory": 1,
        "ip4Addr": "10.11.220.{}".format(resName),
        "protocolPort": json.dumps([{"protocols": "ssh", "port": 22, "established": "true"}, {"protocols": "sftp", "port": 22, "established": "true"}])
    }

    print(businesdata)
    # koal.it_assert.add_assert(json=businesdata)