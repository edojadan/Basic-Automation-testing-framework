from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL

class SearchPage(BasePage):
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    RESULT_STATS = (By.ID, "result-stats")

    def load(self):
        self.driver.get(BASE_URL)

    def search(self, query):
        self.find_element(self.SEARCH_FIELD).send_keys(query)
        self.find_element(self.SEARCH_BUTTON).click()

    def verify_results(self):
        return self.find_element(self.RESULT_STATS) is not None