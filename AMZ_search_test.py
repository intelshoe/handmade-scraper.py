#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

import time 

# start firefox
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',options=options)

time.sleep(20)

driver.get("https://www.amazon.com") # open amazon.com

time.sleep(40)

assert "Amazon.com" in driver.title # make sure Amazon is in page title

# Find search box, enter search term and press enter
elem = driver.find_element_by_name("field-keywords")

time.sleep(5)

elem.clear()
elem.send_keys("handmade")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source # make sure some results found

driver.close()