from pages import LoginPage

class LoginActions:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def LoginUser(self, email, password):
        self.login_page.enter_login_email(email)
        self.login_page.enter_password(password)