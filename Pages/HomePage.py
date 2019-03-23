class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.logout = "//*[@id='logoutLink']"

    def enter_logout(self):
        self.driver.find_element_by_xpath(self.logout).click()