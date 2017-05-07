from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm


# Create your views here.

def home_page(request):
    # 访问首页
    # /
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    # 访问列表页，或者是提交新的事项到目标列表
    # /lists/<id>/
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(list_item=list_, text=request.POST['text'])
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error, 'form': ItemForm()})

def new_list(request):
    # 创建新的事项列表，重定向到列表页
    if request.method == 'POST':
        list_ = List.objects.create()
        item = Item(list_item=list_, text=request.POST['text'])
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {'error': error, 'form': ItemForm()})
        return redirect(list_)