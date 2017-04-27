from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


EXECUTABLE_DRIVER = 'phantomjs'

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        if EXECUTABLE_DRIVER == 'chrome':
            self.browser = webdriver.Chrome(executable_path='../chromedriver.exe')
        else:
            self.browser = webdriver.PhantomJS(executable_path='../phantomjs.exe')
        #self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看网站的首页
        self.browser.get(self.live_server_url)    

        # 首页的标题和头部有着'To-DO'这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 网站需要输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 在文本框输入待办事项"Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        # 按回车键后，页面更新了
        # 待办事项表格显示"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面又显示了一个文本框，可以输入其它待办事项
        # 输入"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，清单显示了这两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # 网站需要记住事项清单
        # 需要为每个用户生成唯一的id
        # 页面需要解释性文本

        self.fail('Finish the test!')



