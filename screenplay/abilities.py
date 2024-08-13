from .base_classes import Ability
from selenium.webdriver.remote.webdriver import WebDriver

class BrowseTheWeb(Ability):
    def __init__(self, driver: WebDriver):
        self.driver = driver