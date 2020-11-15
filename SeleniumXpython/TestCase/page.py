from locator import MainPageLocators,SearchResultsPageLocators
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BassPage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BassPage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLoactors.GO_BUTTON)
        element.click()

class SearchResultPage(BassPage):
    def is_result_found(self):
        return "No Results Found." not in self.driver.page_source