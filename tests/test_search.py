from pages.search_page import SearchPage

def test_search_functionality(browser):
    search_page = SearchPage(browser)
    search_page.load()
    search_page.search("Selenium Python")
    assert search_page.verify_results()