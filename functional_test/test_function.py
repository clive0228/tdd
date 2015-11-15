from selenium import webdriver

import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # connecting website
        self.browser.get('http://localhost:8000')
        
        # check title of website
        self.assertIn('To-Do', self.browser.title)
        # self.fail("Test Finished!")

        # terminate website

if __name__ == '__main__':
    unittest.main(warnings='ignore')
