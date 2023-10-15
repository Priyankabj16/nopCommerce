import faulthandler
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities import XlUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test002_DDT_Login:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    path = "TestData/pydatadriven.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self):
        self.logger.info("  Test_002_login_ddt test")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.clickverificationcheckbox()
        self.lp.clickAdminarea()

        self.rows = XlUtils.getRowcount(self.path, 'Sheet1')
        print("number of rows in Excel:", self.rows)
        # empty list variable
        list_status = []
        for r in range(2, self.rows + 1):
            self.user = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("  Test Passed")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("  Test Failed")
                    self.lp.clickLogout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("  Test Failed")
                    list_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("  Test Passed")
                    list_status.append("Pass")
                print(list_status)
        if "Fail" not in list_status:
            self.logger.info("  Login ddt Test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("  Login ddt Test Failed")
            self.driver.close()
            assert False
        self.logger.info("  End of Login DDT Test")
        self.logger.info("  Completed  TC_LoginDDT_002")
