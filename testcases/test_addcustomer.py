import random
import string
import faulthandler
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Addcustomerpage import AddCustomer
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))


class Test_003_Addcustomer:
    faulthandler.disable()
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self):
        self.logger.info("  Test_003_Addcustomer")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("  Launching Login Page")
        self.lp = LoginPage(self.driver)
        self.lp.clickverificationcheckbox()
        self.lp.clickAdminarea()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("  Launched Login Page")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("  Adding New Customer")
        self.addcust.clickAddnew()

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setManagerOfVebdor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Vikas")
        self.addcust.setLastName("Shetty")
        self.addcust.setdob("01/16/1999")
        self.addcust.setCompanyName("abcd")
        self.addcust.setAdminContent("This is sample....")
        self.addcust.clickOnSave()

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("  Successfully added customer")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error(" Test Unsuccessful")
            assert False
