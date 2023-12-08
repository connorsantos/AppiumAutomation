from appium.webdriver.common.appiumby import AppiumBy

from views.base_view import BaseView

class NodeQueryView(BaseView):
    
    ITEM_BOX = "/following-sibling::android.widget.CheckBox"
    TAKE_OUT_TRASH_ITEM = (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='Task Take out Trash']"+ITEM_BOX)
    DO_LAUNDRY_ITEM = (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='Task Do Laundry']"+ITEM_BOX)

    def check_trash_box(self):
        self.wait_for(self.TAKE_OUT_TRASH_ITEM).click()
   
    def get_trash_box_item(self):
        return self.find(self.TAKE_OUT_TRASH_ITEM).get_attribute('checked')