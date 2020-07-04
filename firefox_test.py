# pip install -U selenium
import time

from selenium import webdriver
# THis comment is to modify the file to check its git status
# second comment to see the file at different places in git status
# This change is made after creating repo in GitHub to see if this
# line gets reflected on the server after push
driver = webdriver.Firefox(executable_path="../resources/geckodriver-64bit.exe")
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com")
driver.find_element_by_id("loginname").send_keys("stc123")
driver.find_element_by_id("loginpassword").send_keys("12345")
driver.find_element_by_id("loginbutton").click()
time.sleep(4)
#driver.

print(driver.title)
# driver.

driver.close()