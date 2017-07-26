# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class doska(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_doska(self):
        success = True
        wd = self.wd
        wd.get("https://doska.io/")
        wd.find_element_by_name("search_text").click()
        wd.find_element_by_name("search_text").clear()
        wd.find_element_by_name("search_text").send_keys("iphone")
        wd.find_element_by_xpath("//form[@id='form-search']/fieldset/input").click()
        wd.find_element_by_link_text("Продам iPhone 5 16GB MD297CS/A").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
