from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Item.objects.create(list=list_, text=request.POST['item_text'])
        return redirect('/lists/%d/' % (list_.id, ))

def add_item(request, list_id):
    if request.method == 'POST':
        list_ = List.objects.get(id=list_id)
        Item.objects.create(list=list_, text=request.POST['item_text'])
        return redirect('/lists/%d/' % (list_.id, ))