from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 访问首页，不小心提交了空待办事项
        # 输入框为空，按下了回车键

        # 首页刷新，显示一个错误消息
        # 提示待办事项不能为空

        # 输入一些文字，再次提交，这次成功了

        # 又提交了一个空的待办事项

        # 错误消息再次出现
        self.fail('write me')
