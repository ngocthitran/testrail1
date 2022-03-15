import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage():
    driver = None
    logger = None


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.pre_get_elements()
        self.get_elements()
        self.post_get_elements()


    def get_elements(self):
        pass


    def pre_get_elements(self):
        pass


    def post_get_elements(self):
        pass


    def get_current_url(self):
        return self.driver.current_url





