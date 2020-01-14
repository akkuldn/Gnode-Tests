"""
This class consists of various checkboxes,input fields and buttons that would be used to automate the Discover Music component of Gnod website
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class GnodMusic_Objects:
    "Page object for the discoverm usic"
    
    discover_music=locators.discover_music
    continue_button=locators.continue_button
    textbox1=locators.textbox1
    textbox2=locators.textbox2
    textbox3=locators.textbox3
    submit_button=locators.submit_button
    like_button=locators.like_button
    dislike_button=locators.dislike_button
    dont_know_button=locators.dont_know_button
    result=locators.music_result

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def discover_music_menu(self,wait_seconds=2):
        "Function to get to the discover music page from the homepage"
        
        #Click on Discover music menu
        result_flag = self.click_element(self.discover_music)
        self.wait(wait_seconds)
        self.switch_window()
        self.wait(wait_seconds)

        #Click on continue button
        result_flag &= self.click_element(self.continue_button)
        
        self.conditional_write(result_flag,
        positive='Successfully entered the discover music page',
        negative='Failed to access the discover music page',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def fill_out_form(self,musician1,musician2,musician3,wait_seconds=1):
        "Fuction to fill the form by entering strings into the textboxes and clicking the submit button"

        #Enter string into textbox1
        result_flag = self.set_text(self.textbox1,musician1)

        self.wait(wait_seconds)
        
        #Enter string into textbox2
        result_flag &= self.set_text(self.textbox2,musician2)

        self.wait(wait_seconds)

        #Enter string into textbox3
        result_flag &= self.set_text(self.textbox3,musician3)

        self.wait(wait_seconds)
        
        #click on the submit button
        result_flag &= self.click_element(self.submit_button)

        self.wait(wait_seconds)

        #check if result element is displayed after submitting the form
        result_flag &= self.check_element_displayed(self.result)

        self.conditional_write(result_flag,
        positive='submitted the form and obtained the result',
        negative='failed to submit the form',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def respond_to_result(self,wait_seconds=3):
        "Fuction to check the three response buttons to the results displayed in discover music"

        #click on like button
        result_flag = self.click_element(self.like_button)

        self.conditional_write(result_flag,
        positive='Clicked on the like button',
        negative='Failed to click the like button',
        level='debug')
        
        self.wait(wait_seconds)
        
        #click the dislike button
        result_flag &= self.click_element(self.dislike_button)

        self.conditional_write(result_flag,
        positive='Clicked on the dislike button',
        negative='Failed to click the dislike button',
        level='debug')

        self.wait(wait_seconds)

        #click the Dont Know button
        result_flag &=self.click_element(self.dont_know_button)

        self.conditional_write(result_flag,
        positive='Clicked on the Dont know button',
        negative='Failed to click the Dont Know button',
        level='debug')

        return result_flag
    