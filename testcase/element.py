from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):
    '''Represents one element on the page'''

    def __set__(self, obj, value):
        '''Set the value for an element'''
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator)
        )
        # Clear element then send value
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        '''Gets value for element'''
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator)
        )
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute('value')
