import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import page


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://www.python.org')

    def tearDown(self):
        self.driver.close()

    def test_title(self):
        assert page.MainPage(self.driver).is_title_matching()

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matching()
        mainPage.search_text_element = 'pycon'
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

if __name__ == '__main__':
    unittest.main()
