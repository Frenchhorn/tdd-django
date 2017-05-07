from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List
from django.db.utils import IntegrityError

# 测试Item对象
class ItemModelsTest(TestCase):

    # 测试Item对象text的默认值
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    # 测试Item对象的外键list_item
    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list_item = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    # Item对象的text不能为空值
    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list_item=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    # 向同一事项列表提交同一事项，应该抛出错误
    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list_item=list_, text='test')
        with self.assertRaises(IntegrityError):
            item = Item(list_item=list_, text='test')
            #item.full_clean()
            item.save()

    # 向不同事项列表提交相同事项，不应抛出错误
    def test_CAN_save_same_item_to_defferent_lists(self):
        list_a = List.objects.create()
        list_b = List.objects.create()
        Item.objects.create(list_item=list_a, text='test')
        item = Item(list_item=list_b, text='test')
        item.full_clean()   #不应抛出错误

# 测试List对象
class ListModelsTest(TestCase):

    # 测试List对象的get_absolute_url方法是否返回正确的URL
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id,))