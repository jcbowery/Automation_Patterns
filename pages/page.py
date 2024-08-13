from typing import Any
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, driver :WebDriver):
        self.driver = driver
    
    def __getattribute__(self,name) -> WebElement :
        attr = object.__getattribute__(self,name)
        if isinstance(attr, tuple):
            if len(attr) == 2 and attr[0] in [By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME, By.XPATH]:
                return self.driver.find_element(*attr)
        return attr