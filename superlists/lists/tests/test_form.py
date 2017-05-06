from django.test import TestCase

from lists.forms import ItemForm, ItemFormAPI, EMPTY_LIST_ERROR

class ItemFormTest(TestCase):

    # 这个测试与该项目无关，仅为探索相关的API
    def test_form_renders_item_text_input_api(self):
        form = ItemFormAPI()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())  # form.as_p()的作用是把表单渲染成HTML
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    # 提交空待办事项时，表单不会保存数据
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())   # form.is_valid()判断表单是否有效，返回True或False
        self.assertEqual(   # 显示指定错误信息
            form.errors['text'],    # is_valid方法会生成errors属性，把字段映射到该字段的错误列表上
            [EMPTY_LIST_ERROR]
        )