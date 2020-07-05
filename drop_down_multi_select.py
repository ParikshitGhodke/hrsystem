# pip install -U selenium
import time
import unittest #https://docs.python.org/3.4/library/unittest.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class HandleDropDown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run only once before the setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will run only once after the tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../resources/chromedriver-81.exe")
        self.driver.maximize_window()

    def test_combo(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        make = self.driver.find_element_by_name("make")
        make = Select(make)
        time.sleep(2)
        make.select_by_value("audi")
        time.sleep(2)
        make.select_by_index(1)
        time.sleep(2)
        make.select_by_visible_text("Honda")
        time.sleep(3)
        #print("Is it a multiple Select? ",make.is_multiple)
        #print("How many options are there inside combo?", len(make.options))
        print(type(make.options))
        print(make.options)
        expected_options = ["BMW", "Mercedes","Audi","Honda"]

        #
        #print(make.options[0])
        #print(type(make.options[0]))
        actual_options = []
        for i in make.options:
            actual_options.append(i.text)
        #print("Current Selected Option is - ", make.first_selected_option.text)
        self.assertListEqual(actual_options,expected_options)

    def test_which_fails(self):
        self.assertTrue(False)

    def test_multi_select(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        color = self.driver.find_element_by_name("color")
        make = Select(color)
        make.select_by_value("wt")
        make.select_by_value("br")
        make.select_by_visible_text("Silver")
        #print("No. of optoins selected",len(make.all_selected_options))
        expected_selected_colors = ["White", "Brown", "Silver"]
        actual_selected_colors = []
        for i in make.all_selected_options:
            actual_selected_colors.append(i.text)
        self.assertListEqual(actual_selected_colors, expected_selected_colors)

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
