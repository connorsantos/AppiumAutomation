from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomeView(object):
    ACCESSABILITY_ITEM = (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility"]')

    def __init__(self, driver):
         self.driver=driver

    def nav_to_accessability(self):
         wait = WebDriverWait(self.driver, 10)
         wait.until(EC.presence_of_element_located((self.ACCESSABILITY_ITEM))).click()