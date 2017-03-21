import unittest
from oss.pages.ossloginpage import Oss_login
from oss.pages.CustmBuyerOSSSearch import CustmBuyerOSSSearch
from oss.pages.DevSearchResult import DeviceSearchResult
from oss.pages.customers.CustDetails1 import CustomerDetailsPage
from selenium import webdriver
from oss.setup.config_oss import JsonConfig

#Unittest framework for testing the OSS Functionalities
class OSStest(unittest.TestCase):

    def setUp(self):
        print "Setting up OSS Test Automation"
        #Loading the Json configuration details
        jsonobj = JsonConfig()
        self.jconfig = jsonobj.dump_config()

        self.driver = webdriver.Firefox()
        self.driver.get(self.jconfig["sandbox"]["oss_url"])

    def test_Cancel(self):
        print "OSS Cancel Testcase Executing"
        oss_obj = Oss_login(self.driver)

        #Fetching the OSS Access credentials & Myxid
        username = self.jconfig["oss_login"]["username"]
        password = self.jconfig["oss_login"]["password"]
        myxid = self.jconfig["device_credentials"]["myxid"]
        oss_obj.oss_login(username, password)

        myxid_obj = CustmBuyerOSSSearch(self.driver)
        myxid_obj.myxid_look(myxid)
        dev_obj = DeviceSearchResult(self.driver)
        dev_obj.access_registrant()
        cust_obj = CustomerDetailsPage(self.driver)
        cust_obj.cancel_click()
        self.driver.close()

    def tearDown(self):
        pass
        #  self.driver.quit()


if __name__ == "__main__":
    unittest.main()