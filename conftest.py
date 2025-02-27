import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def browser(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()