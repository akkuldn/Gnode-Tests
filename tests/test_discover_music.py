"""
This is an automated test for Discover Music component of Gnod.com, the test involves entering the discover music page,filling out and submitting the form,checking the response buttons
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import pytest
import conf.Gnod_conf as conf


@pytest.mark.GUI
def test_product_chart(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        
        #Set start_time with current time
        start_time = int(time.time())	

        test_obj = PageFactory.get_page_object("gnod")

        #Get the musician's names from conf file
        musician1=conf.musician1
        musician2=conf.musician2
        musician3=conf.musician3

        #Get to the discover music page
        result_flag=test_obj.discover_music_menu()

        test_obj.log_result(result_flag,positive='Successfully landed on discover music page',
        negative='could not access the discover music page') 

        #fill out the form in discover music page and hit the submit button
        result_flag=test_obj.fill_out_form(musician1,musician2,musician3)
        
        test_obj.log_result(result_flag,positive='Successfully submitted the form',
        negative='could not submit the form') 

        #check if all the response buttons work correctly
        result_flag=test_obj.respond_to_result()
        
        test_obj.log_result(result_flag,positive='All the response buttons worked fine',
        negative='The response buttons did not work') 

        #13. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter        

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    
    assert expected_pass == actual_pass, "Test failed: %s"%__file__

    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)


        test_product_chart(test_obj)
                
        #teardowm
        test_obj.wait(3)
        test_obj.teardown() 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())