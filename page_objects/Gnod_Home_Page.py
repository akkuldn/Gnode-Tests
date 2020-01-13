"""
This redirects us to the Home page of the Gnod website.
URL: http://www.gnod.com/
"""
from .Base_Page import Base_Page
from .Productchart_Objects import Productchart_Objects
from .GnodMusic_Objects import GnodMusic_Objects
from .Moviemap_Objects import Moviemap_Objects

class Gnod_Home_Page(Base_Page,Productchart_Objects,GnodMusic_Objects,Moviemap_Objects):
    "Page Object for the productchart page"
    
    def start(self):
        "Use this method to go to specific URL -- if needed"
        
        url=" "
        self.open(url)