from django.shortcuts import render

# access item model
from .models import Item


# Create your views here.


def get_todo_list(request):
    # get query set of items in db
    items = Item.objects.all()
    # context is variable for dictionary of all items
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
