import pytest
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages import LoginPage
from actions import LoginActions
from screenplay import Actor, BrowseTheWeb, Login


def test_login_pom():
    # setup
    driver:WebDriver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/login")

    # perform test actions. focus here
    lp = LoginPage(driver)
    lp.enter_login_email("abc@abc.com")
    lp.enter_password("abc123")
    lp.click_login_button()

    # close down
    time.sleep(2)
    driver.quit()

def test_login_actions():
    # setup
    driver:WebDriver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/login")

    # perform test actions. focus here
    login_actions = LoginActions(driver)
    login_actions.LoginUser("abc@abc.com", "abc123")

    # close down
    time.sleep(2)
    driver.quit()

def test_login_screenplay():
    # setup
    driver:WebDriver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://automationexercise.com/login")
    john = Actor("John", driver).can(BrowseTheWeb(driver))

    # perform test actions. focus here
    john.attempts_to(
        Login("abc@abc.com", "abc123")
    )

    # close down
    time.sleep(2)
    driver.quit()