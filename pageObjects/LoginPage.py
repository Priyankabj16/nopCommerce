from selenium.webdriver.common.by import By


class BaseTest:
    pass


class LoginPage(BaseTest):
    
    verification_checkbox_xpath = "//input[@type='checkbox']"
    admin_area_xpath = "//span[normalize-space()='Admin area']"
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@class='password']"
    button_login_css = "button[type='submit']"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickverificationcheckbox(self):
        self.driver.find_element(By.XPATH, self.verification_checkbox_xpath).click()

    def clickAdminarea(self):
        self.driver.find_element(By.XPATH, self.admin_area_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
