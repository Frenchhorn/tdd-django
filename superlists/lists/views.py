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
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)

    return render(request, 'list.html', {'list': list_, 'form': form})

def new_list(request):
    # 创建新的事项列表，重定向到列表页
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            list_ = List.objects.create()
            form.save(for_list=list_)
            return redirect(list_)
        else:
            return render(request, 'home.html', {'form': form})