from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time

TEST_URL = "https://techwithtim.net"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Brave: driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))

driver.get(TEST_URL)
print(driver.title)


def find_tutorial():
    link = driver.find_element(By.LINK_TEXT, "Tutorials")
    link.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "python programming"))
        )
        element.click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button__ButtonStyled-sc-73bwj8-0 hZeIKp"))
        )
        element.click()
    except:
        driver.quit()


def find_blog_post():
    search = driver.find_element(by=By.NAME, value="s")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)

    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        articles = main.find_elements(By.TAG_NAME, "article")
        for article in articles:
            header = article.find_element(By.CLASS_NAME, "entry-summary")
            print(header.text)
    except:
        driver.quit()
