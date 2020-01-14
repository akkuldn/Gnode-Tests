"""
This class consists of various input fields and buttons that would be used to automate the movie map component of Gnod website
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Moviemap_Objects:
    "Page object for the movie map"
    
    moviemap_menu=locators.movie_map
    search_bar=locators.search_bar
    search_button=locators.search_button
    nearest_movie=locators.nearest_movie
    moviemap_result=locators.moviemap_result


    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def movie_map(self,wait_seconds=2):
        "Function to get to the movie map page"
        
        #Click on movie map menu
        result_flag = self.click_element(self.moviemap_menu)
        self.wait(wait_seconds)
        self.switch_window()
        
        self.conditional_write(result_flag,
        positive='Successfully entered the movie map page',
        negative='Failed to access the movie map page',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_movie_map(self,movie_name,wait_seconds=2):
        "Fuction to search for a movie in the movie map search bar"

        #enter text into search bar
        result_flag = self.set_text(self.search_bar,movie_name)
        
        self.wait(wait_seconds)
        
        #click the search button
        result_flag &= self.click_element(self.search_button)

        self.wait(wait_seconds)
        
        #verify with an element from the result page if we have successfully landed on the result page
        result_flag &= self.check_element_displayed(self.moviemap_result)

        self.conditional_write(result_flag,
        positive='search query submitted successfully',
        negative='Failed to submit search query',
        level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_nearest_movie(self,wait_seconds=3):
        "Fuction to select the nearest movies from the selected movie"

        self.wait(wait_seconds)
        #click on nearest movie
        result_flag = self.click_element(self.nearest_movie)
        
        self.wait(wait_seconds)
        
        #click the nearest movie again
        result_flag &= self.click_element(self.nearest_movie)

        self.conditional_write(result_flag,
        positive='successfully selected the nearest movie',
        negative='Failed to select the nearest movie',
        level='debug')

        return result_flag
    