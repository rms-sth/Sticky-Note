from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ToDoItem


def todo_list(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, "todo.html", {"all_items": all_todo_items})


def todo_create(request):
    if request.method == "POST":
        new_item = ToDoItem(content=request.POST["content"])
        new_item.save()
        return HttpResponseRedirect("/")


def todo_delete(request, pk):
    delete_item = ToDoItem.objects.get(pk=pk)
    delete_item.delete()
    return HttpResponseRedirect("/")
