from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 查看网站的首页
        self.browser.get(self.server_url)    

        # 首页的标题和头部有着'To-DO'这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 网站需要输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 在文本框输入待办事项"Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        # 按回车键后，页面更新了，跳到一个新的URL
        # 这个页面的待办事项表格显示"1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        first_list_url = self.browser.current_url
        self.assertRegex(first_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 页面又显示了一个文本框，可以输入其它待办事项
        # 输入"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面再次更新，清单显示了这两个待办事项
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        ## 使用一个新的浏览器会话
        self.browser.quit()
        self.initBrowser()

        # 一个新用户访问首页，看不到其它用户的待办事项
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text)
        

        # 新用户输入一个新事项，新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 新用户获得他的URL，两个URL不一样
        second_list_url = self.browser.current_url
        self.assertRegex(second_list_url, '/lists/.+')
        self.assertNotEqual(first_list_url, second_list_url)
        # 可以看到他的事项
        self.check_for_row_in_list_table('1: Buy milk')
        # 看不到其他人的事项
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text)