import time
from appium import webdriver
from os import path
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'API Demos_4.0_apkcombo.com.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android', 
    'deviceName': 'Android Device',
    'automationName': 'UiAutomator2',
    'app': APP
}
option = AppiumOptions().load_capabilities(CAPS)
driver = webdriver.Remote(
    command_executor=APPIUM,
    options=option
)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility"]'))).click()
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Querying"]'))).click()
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="com.hmh.api:id/tasklist_finished"])[1]'))).click()
    box = driver.find_element(AppiumBy.XPATH, 
                    '(//android.widget.CheckBox[@resource-id="com.hmh.api:id/tasklist_finished"])[1]').get_attribute('checked')
    print(box)
    assert box is not True
    #wait.until(EC.presence_of_element_located(
    #    (AppiumBy.ACCESSIBILITY_ID, 'Login Screen')))
    #driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
    #driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Accessibility"]')
finally:
    driver.quit()