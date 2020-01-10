#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Discover Music component
discover_music="xpath,//A[@href='http://www.gnoosic.com']"
continue_button="xpath,//A[@class='continue'][text()='continue']"
textbox1="xpath,(//INPUT[@type='text'])[1]"
textbox2="xpath,(//INPUT[@type='text'])[2]"
textbox3="xpath,(//INPUT[@type='text'])[3]"
submit_button="xpath,//INPUT[@type='submit']"
like_button="xpath,//INPUT[@class='like_yes']"
dislike_button="xpath,//INPUT[@class='like_no']"
dont_know_button="xpath,//INPUT[@class='like_dunno']"

#Locators for the  productchart component
productchart="xpath,//H3[text()='Product Chart']"
smartphone_tab="xpath,(//A[@class='product'])[1]"
brand_menu="xpath,//A[@id='toggle_brand']"
samsung_checkbox="xpath,(//INPUT[@type='checkbox'])[32]"
os_menu="xpath,//A[@id='toggle_os']"
android_checkbox="xpath,(//INPUT[@type='checkbox'])[1]"