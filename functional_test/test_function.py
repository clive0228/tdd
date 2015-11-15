from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # connecting website
        self.browser.get(self.live_server_url)

        # check title of website
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # add job
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            "input job item"
        )

        # buying craft feather
        inputbox.send_keys("buying craft feather")

        # renew website and show first job
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("1: buying craft feather")

        # add another item in list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("making web using craft feather")
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table("2: making web using craft feather")
        self.check_for_row_in_list_table("1: buying craft feather")

        # terminate website
        # self.fail('finish the test')
