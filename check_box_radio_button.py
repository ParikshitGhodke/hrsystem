# pip install -U selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../resources/chromedriver-81.exe")
driver.maximize_window()
driver.get("http://cookbook.seleniumacademy.com/Config.html")
driver.find_element_by_css_selector("input[value='Diesel']").click()
time.sleep(4)

airbags = driver.find_element_by_name("airbags")

if not airbags.is_selected():
    airbags.click()
time.sleep(4)

if airbags.is_selected():
    airbags.click()
time.sleep(4)


