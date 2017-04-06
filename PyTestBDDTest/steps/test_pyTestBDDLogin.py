import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
import allure


@pytest.fixture(scope="module")
def driver():
    """Create fixture"""
    fixture = webdriver.Chrome('C:\\Users\\tsaytieva\\Documents\\Python\\Drivers\\chromedriver.exe')
    return fixture


@allure.feature('login as oneday admin')
@scenario('pyTestBDDLogin.feature', 'login as oneday admin')
def test_login():
    pass


@pytest.allure.step
@given('login page "http://cms.oneday.com/Admin/Account/Login"')
def login_page(driver):
    driver.get("http://cms.oneday.com/Admin/Account/Login")


@pytest.allure.step
@when('user enters login: "jdineshk@gmail.com" and password: "brookdale2016"')
def enter_credentials(driver):
    driver.find_element_by_id('Email').send_keys('jdineshk@gmail.com')
    driver.find_element_by_id('Password').send_keys('brookdale2016')


@pytest.allure.step
@when('submits')
def login_submit(driver):
    driver.find_element_by_xpath('//div/button[@type="submit"]').click()


@pytest.allure.step
@then('user sees "http://cms.oneday.com/Admin/Company" page')
def company_page_shown(driver):
    assert 'http://cms.oneday.com/Admin/Company'.__eq__(driver.current_url)
    allure.attach('Company page', driver.get_screenshot_as_png(), allure.attach_type.PNG)

