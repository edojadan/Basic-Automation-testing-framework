from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    assert "dashboard" in browser.current_url