from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 输入框居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('testing')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,
            512,
            delta=5
        )