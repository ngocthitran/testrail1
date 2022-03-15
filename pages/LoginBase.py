from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.BasePage import *
import consts

_email_locator = (By.XPATH, "//input[@name = 'email']")
_password_locator = (By.XPATH, "//input[@name = 'password']")
_sign_in_btn_locator = (By.XPATH, "//button[@type = 'submit']")


class LoginBase(BasePage):

    def pre_get_elements(self):
        self.driver.get(consts.URL_Revinate_STAGING_HOME)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name = 'email']")))


    def login(self, credentials):
        txt_email = self.driver.find_element(*_email_locator)
        txt_password = self.driver.find_element(*_password_locator)
        btn_log_in = self.driver.find_element(*_sign_in_btn_locator)

        self.logger.info(f"Trying to login with email {credentials.email}")
        txt_email.send_keys(credentials.email)
        txt_password.send_keys(credentials.password)
        btn_log_in.click()

        time.sleep(5)


    def is_logged(self, credentials):
        logged_email = self.driver.find_element(By.XPATH, f"//a[text()='Applications']")
        return True



