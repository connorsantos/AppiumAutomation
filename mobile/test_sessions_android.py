from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from views.home_view import HomeView

def test_uncheck_box(driver):
    home = HomeView(driver)
    home.nav_to_accessability()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility"]'))).click()
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Querying"]'))).click()
    wait.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '(//android.widget.CheckBox[@resource-id="com.example.android.apis:id/tasklist_finished"])[1]'))).click()
    box = driver.find_element(AppiumBy.XPATH, 
                    '(//android.widget.CheckBox[@resource-id="com.example.android.apis:id/tasklist_finished"])[1]').get_attribute('checked')
    print(box)
    assert box is not True
    #wait.until(EC.presence_of_element_located(
    #    (AppiumBy.ACCESSIBILITY_ID, 'Login Screen')))
    #driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
    #driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Accessibility"]')

