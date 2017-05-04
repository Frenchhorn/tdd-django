from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip


EXECUTABLE_DRIVER = 'phantomjs'
SERVER_URL = ''

class FunctionalTest(StaticLiveServerTestCase):

    def initBrowser(self):
        if EXECUTABLE_DRIVER == 'chrome':
            self.browser = webdriver.Chrome(executable_path='../chromedriver.exe')
        else:
            self.browser = webdriver.PhantomJS(executable_path='../phantomjs.exe')

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    @classmethod
    def setUpClass(cls):
        if SERVER_URL :
            cls.server_url = SERVER_URL
            return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def setUp(self):
        self.initBrowser()

    def tearDown(self):
        self.browser.quit()