from operations.business_system import *

def add_busyness(koal, abisname, workflownodenum,abisadminids):
    koal_ = Business_system_api(koal)
    response = koal_.add_business_system(abisname, workflownodenum,abisadminids)
    if response.success != True:
        return response
    