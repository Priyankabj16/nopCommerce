import pytest
import faulthandler
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_login:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_homepagetitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickverificationcheckbox()
        act_title = self.driver.title
        if act_title == "Store Demo - nopCommerce":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle_scr.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickverificationcheckbox()
        self.lp.clickAdminarea()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_scr.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_logout(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickverificationcheckbox()
        self.lp.clickAdminarea()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickLogout()
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_scr.png")
            self.driver.close()
            assert False
