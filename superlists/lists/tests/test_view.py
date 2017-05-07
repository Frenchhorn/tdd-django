'''
测试视图层

resolve     得到对应URL的对象
found = resolve('/')
self.assertEqual(found.func, home_page)

render_to_string    把对应的template转换为HTML
request = HttpRequest()
response = home_page(request)
expected_html = render_to_string('home.html')
'''
from unittest import skip
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List
from lists.forms import ItemForm, EMPTY_LIST_ERROR

# Create your tests here.

class HomePageTest(TestCase):

    # 测首页的所用的Template
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # 测首页的所用的表单
    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)

class NewListTest(TestCase):
    # 创建新的事项列表
    # /lists/new

    def test_saving_a_POST_request(self):
        self.client.post('/lists/new', data={'text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id, ))

    # 在首页创建新的事项列表时，如果为非法输入值，需要返回首页，且不创建数据
    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    # 在首页创建新的事项列表时，如果为非法输入值，返回首页后，需要有错误信息
    def test_validation_errors_are_show_on_home_page(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertContains(response, escape(EMPTY_LIST_ERROR))

    # 在首页创建新的事项列表时，如果为非法输入值，返回首页时，需要把表单传入模板
    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertIsInstance(response.context['form'], ItemForm)

class ListViewTest(TestCase):
    # 测试列表页
    # /lists/<id>/

    # 辅助方法，返回一个带有非法数值的POST请求
    def post_invalid_input(self):
        list_ = List.objects.create()
        return self.client.post(
            '/lists/%d/' % (list_.id,),
            data={'text': ''}
        )

    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(list_item=correct_list, text='itemey 1')
        Item.objects.create(list_item=correct_list, text='itemey 2')

        other_list = List.objects.create()
        Item.objects.create(list_item=other_list, text='Other itemey 1')
        Item.objects.create(list_item=other_list, text='Othre itemey 2')

        response = self.client.get('/lists/%d/' % (correct_list.id, ))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'Other itemey 1')
        self.assertNotContains(response, 'Other itemey 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id),
            data={'text': 'A new item for existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for existing list')
        self.assertEqual(new_item.list_item, correct_list)

    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/' % (correct_list.id),
            data={'text': 'A new item for existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id))

    # 测试GET请求
    def test_displays_item_form(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % list_.id)
        self.assertIsInstance(response.context['form'], ItemForm)

    # POST请求的数值非法时，不创建数据
    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(), 0)

    # POST请求的数值非法时，返回当前页面
    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

    # POST请求的数值非法时，传递表单到当前页面
    def test_for_invalid_input_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ItemForm)

    # POST请求的数值非法时，返回当前页面，页面有错误信息
    def test_for_invalid_input_show_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_LIST_ERROR))


class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list_item = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list_item = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list_item, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list_item, list_)

