from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccessabilityView(object):
    NODE_QUERYING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Querying"]')

    def __init__(self, driver):
         self.driver=driver

    def nav_to_access_node_query(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((self.NODE_QUERYING))).click()
         