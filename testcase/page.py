from locator import *
from element import BasePageElement

'''Helpers define pages to test'''

class SearchTextElement(BasePageElement):
    '''Finds element q which identifies search text box'''
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matching(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        # * is a splat or unpack syntax that enumerates tuples
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):
    def is_results_found(self):
        return 'No results found.' not in self.driver.page_source
