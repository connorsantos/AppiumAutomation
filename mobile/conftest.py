import pytest
from os import path
from appium.options.common import AppiumOptions
from appium import webdriver

from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'API Demos_4.0_apkcombo.com.apk')
APPIUM = 'http://localhost:4723'

@pytest.fixture
def driver():
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
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return HomeView(driver)