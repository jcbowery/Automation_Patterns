from selenium.webdriver.remote.webdriver import WebDriver

class Actor:
    def __init__(self, name: str, driver: WebDriver):
        self.name = name
        self.driver = driver
        self.abilities = []

    def can(self, ability):
        self.abilities.append(ability)
        return self
    
    def attempts_to(self, task):
        task.perform_as(self)

class Task:
    def perform_as(self, actor):
        pass

class Question:
    def answer_ass(self, actor):
        pass

class Ability:
    pass

