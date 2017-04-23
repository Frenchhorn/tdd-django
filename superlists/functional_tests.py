from selenium import webdriver
import unittest

EXECUTABLE_DRIVER = 'phantomjs'

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if EXECUTABLE_DRIVER == 'chrome':
            self.browser = webdriver.Chrome(executable_path='../chromedriver.exe')
        elif EXECUTABLE_DRIVER == 'phantomjs':
            self.browser = webdriver.PhantomJS(executable_path='../phantomjs.exe')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看网站的首页
        self.browser.get('http://localhost:8000')    

        # 首页的标题有着'To-DO'这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')



