import pages
from .base_classes import Task

class Login(Task):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        actor.attempts_to(EnterUsername(self.username))
        actor.attempts_to(EnterPassword(self.password))
        actor.attempts_to(ClickLoginButton())

class EnterUsername(Task):
    def __init__(self, username: str):
        self.username = username

    def perform_as(self, actor):
        login_page = pages.LoginPage(actor.driver)
        login_page.enter_login_email(self.username)

class EnterPassword(Task):
    def __init__(self, password: str):
        self.password = password

    def perform_as(self, actor):
        login_page = pages.LoginPage(actor.driver)
        login_page.enter_password(self.password)

class ClickLoginButton(Task):
    def perform_as(self, actor):
        login_page = pages.LoginPage(actor.driver)
        login_page.click_login_button()