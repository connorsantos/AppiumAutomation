from appium.webdriver.common.appiumby import AppiumBy

from views.base_view import BaseView
from views.accessability_view import AccessabilityView

class HomeView(BaseView):
     ACCESSABILITY_ITEM = (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility"]')

     def nav_to_accessability(self):
          self.wait_for(self.ACCESSABILITY_ITEM).click()
          return AccessabilityView(self.driver)