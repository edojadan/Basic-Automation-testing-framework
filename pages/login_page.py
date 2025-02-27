from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")

    def load(self):
        self.driver.get(BASE_URL + "/login")

    def login(self, username, password):
        self.find_element(self.USERNAME_FIELD).send_keys(username)
        self.find_element(self.PASSWORD_FIELD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()