from appium.webdriver.common.appiumby import AppiumBy

from views.base_view import BaseView
from views.node_query_view import NodeQueryView

class AccessabilityView(BaseView):
    NODE_QUERYING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Accessibility Node Querying"]')

    def nav_to_access_node_query(self):
        self.wait_for(self.NODE_QUERYING).click()
        return NodeQueryView(self.driver)
         