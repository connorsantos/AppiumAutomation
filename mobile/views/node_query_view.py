from appium.webdriver.common.appiumby import AppiumBy
from constants.node_query_constants import NodeQueryConstants
from views.base_view import BaseView

class NodeQueryView(BaseView):
    
    TRASH_BOX =   (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.TRASH_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    LAUNDRY_BOX = (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.LAUNDRY_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    CONQUER_BOX = (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.CONQUER_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    NAP_BOX =     (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.NAP_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    TAXES_BOX =   (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.TAXES_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    IRS_BOX =     (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.IRS_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
    TEA_BOX =     (AppiumBy.XPATH,"//android.widget.TextView[@content-desc='"+NodeQueryConstants.TEA_LABEL+"']"+NodeQueryConstants.ITEM_BOX)
        
    def check_box(self, item):
        self.clickItem(item)

    def get_attr(self,item,attr):
        return self.getattr(item,attr)

    def get_current_boxes_states(self):
     return {
        'trash_box': self.get_attr(self.TRASH_BOX,'checked'),
        'laundry_box': self.get_attr(self.LAUNDRY_BOX,'checked'),
        'conquer_box': self.get_attr(self.CONQUER_BOX,'checked'),
        'nap_box': self.get_attr(self.NAP_BOX,'checked'),
        'taxes_box': self.get_attr(self.TAXES_BOX,'checked'),
        'irs_box': self.get_attr(self.IRS_BOX,'checked'),
        'tea_box': self.get_attr(self.TEA_BOX,'checked'),
    }