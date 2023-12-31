from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time


def find_cookie(driver):
    return driver.find_element(by=By.ID, value='bigCookie')

def find_cookie_count(driver):
    return driver.find_element(by=By.ID, value='cookies')

TEST_URL = "https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Brave: driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

driver.get(TEST_URL)
driver.implicitly_wait(5)

english = driver.find_element(By.ID, "langSelect-EN")
english.click()

items = [driver.find_element(by=By.ID, value="productPrice" + str(i)) for i in range(1,-1,-1)]
actions = ActionChains(driver)

for i in range(9001):
    # Getting cookie inside loop prevents StaleElementReferenceException
    cookie = find_cookie(driver)
    actions.click(cookie)
    actions.perform()
    cookie_count = find_cookie_count(driver)
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    print(count)
