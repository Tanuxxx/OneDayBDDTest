from behave import *
from selenium import webdriver


@given('login page "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome('C:\\Users\\tsaytieva\\Documents\\Python\\Drivers\\chromedriver.exe')
    context.driver.get(url)


@when('user enters login: "{email}" and password: "{password}"')
def step_impl(context, email, password):
    context.driver.find_element_by_id('Email').send_keys(email)
    context.driver.find_element_by_id('Password').send_keys(password)


@when('submits')
def step_impl(context):
    context.driver.find_element_by_xpath('//div/button[@type="submit"]').click()


@then('user sees "{url}" page')
def step_impl(context, url):
    assert url.__eq__(context.driver.current_url)
