from  Test_Data.Data import *

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.un_locator = "username"
        self.pwd_locator = "pwd"
        self.xpath_locator = "//*[@id='loginButton']/div"

    def enter_un(self):
        self.driver.find_element_by_id(self.un_locator).send_keys(UN)

    def enter_pwd(self):
        self.driver.find_element_by_name(self.pwd_locator).send_keys(PWD)

    def enter_submit(self):
        self.driver.find_element_by_xpath(self.xpath_locator).click()
