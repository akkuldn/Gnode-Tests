"""
This class consists of various checkboxes,input fields and buttons that would be used to automate the productchart component of Gnod website
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Productchart_Objects:
    "Page object for the product_chart"
    
    productchart=locators.productchart
    smartphone_tab=locators.smartphone_tab
    product_brand=locators.brand_menu
    brand_checkbox=locators.samsung_checkbox
    os_menu=locators.os_menu
    os_checkbox=locators.android_checkbox

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def productchart_smartphone(self,wait_seconds=2):
        "Function to get to the smartphone category under the product cart"
        
        #Click on productchart menu
        result_flag = self.click_element(self.productchart)
        self.wait(wait_seconds)
        self.switch_window()
        self.wait(wait_seconds)

        #Click on Smartphone Tab
        result_flag &= self.click_element(self.smartphone_tab)
        
        self.conditional_write(result_flag,
        positive='Successfully entered the smartphone category of product chart page',
        negative='Failed to access the product chart',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def filter_product_brand(self,wait_seconds=1):
        "Fuction to select and filter the smartphones based on brand"

        #click on brand button
        result_flag = self.click_element(self.product_brand)
        
        self.wait(wait_seconds)
        
        #click the samsung checkbox
        result_flag &= self.click_element(self.brand_checkbox)

        self.conditional_write(result_flag,
        positive='Filtered the products based on brand',
        negative='Failed to filter the products',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def filter_product_os(self,wait_seconds=1):
        "Fuction to select and filter the smartphones based on os"

        #click on os button
        result_flag = self.click_element(self.os_menu)
        
        self.wait(wait_seconds)
        
        #click the android checkbox
        result_flag &= self.click_element(self.os_checkbox)

        self.conditional_write(result_flag,
        positive='Filtered the products based on os',
        negative='Failed to filter the products',
        level='debug')

        return result_flag
    