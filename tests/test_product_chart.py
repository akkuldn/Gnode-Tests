"""
This is an automated test to select the desired specifications to filter the products at https://www.productchart.com
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import pytest


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
        
        #enter smartphone category of the product chart
        result_flag=test_obj.productchart_smartphone() 
        test_obj.log_result(result_flag,positive='Successfully landed on smartphone category of the product_chart',
        negative='could not access the product chart') 

        #set the filter based on brand
        result_flag=test_obj.filter_product_brand() 
        test_obj.log_result(result_flag,positive='Smart phone were successfully filtered based on brand',
        negative='could not filter the smartphones based on brand') 

        #set the filter based on os
        result_flag=test_obj.filter_product_os() 
        test_obj.log_result(result_flag,positive='Smart phone were successfully filtered based on os',
        negative='could not filter the smartphones based on os') 

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