"""
This redirects us to the smartphone category of the productchart website.
URL: https://www.productchart.com/smartphones/
"""
from .Base_Page import Base_Page
from .Productchart_Objects import Productchart_Objects

class Product_Smartphone_Page(Base_Page,Productchart_Objects):
    "Page Object for the productchart page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        
        url="smartphones"
        self.open(url)