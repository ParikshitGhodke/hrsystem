# pip install -U selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../resources/chromedriver-83.exe")
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com")
print(driver.title)
driver.get("http://www.yahoo.in")
driver.back()
driver.forward()
print(driver.name) # Name of the browser (chrome, firefox, ie etc)
driver.find_element(by=By.ID, value='header-search-input').send_keys("Selenium")
driver.current_url
driver.minimize_window()
driver.maximize_window()
print(driver.get_cookies())
driver.delete_cookie('httpOnly')
print(driver.get_cookies())
driver.delete_all_cookies()
print("all",driver.get_cookies())
print(driver.page_source)
driver.refresh()  