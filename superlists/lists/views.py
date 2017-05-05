from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.models import Item, List


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(list_item=list_, text=request.POST['item_text'])
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id, ))
        except ValidationError:
            error = "You can't have an empty list item"
            
    return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        item = Item(list_item=list_, text=request.POST['item_text'])
        try:
            item.full_clean()
            item.save()
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {'error': error})
        return redirect('/lists/%d/' % (list_.id, ))