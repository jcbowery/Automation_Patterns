from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .page import Page

class LoginPage(Page):
    login_email_field = (By.XPATH, "//input[@data-qa='login-email']")
    password_field = (By.NAME, "password")
    login_button = (By.XPATH, "//button[text()='Login']")
    
    def enter_login_email(self, email):
        self.login_email_field.send_keys(email)
    
    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

