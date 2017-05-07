'''
测试表单
'''
from django.test import TestCase
from lists.models import Item, List
from lists.forms import ItemForm, ItemFormAPI, EMPTY_LIST_ERROR
class ItemFormTest(TestCase):

    # 这个测试与该项目无关，仅为探索相关的API
    def test_form_renders_item_text_input_api(self):
        form = ItemFormAPI()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())  # form.as_p()的作用是把表单渲染成HTML
        self.assertIn('class="form-control input-lg"', form.as_p())

    # 测试表单ItemForm的属性
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

    # 测试使用表单来保存数据到数据库
    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list=list_)    # 指定表单属于哪个列表，需要在forms.py重写save方法
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list_item, list_)