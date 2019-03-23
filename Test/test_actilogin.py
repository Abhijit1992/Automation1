from selenium import webdriver
import time
import pytest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Test_Data.Data import *

@pytest.fixture(scope='session')
def test_launch_browser():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/LENOVO/PycharmProjects/Automation 1/Driver/chromedriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)


def test_login(test_launch_browser):
    lp = LoginPage(driver)
    lp.enter_un()
    lp.enter_pwd()
    lp.enter_submit()
    #driver.find_element_by_id("username").send_keys("bubai.mullick")
    #driver.find_element_by_name("pwd").send_keys("ATy9UBE6")
    #driver.find_element_by_xpath("//*[@id='loginButton']/div").click()


def test_logout(test_launch_browser):
    time.sleep(5)
    lo = HomePage(driver)
    lo.enter_logout()
    #driver.find_element_by_xpath("//*[@id='logoutLink']").click()
