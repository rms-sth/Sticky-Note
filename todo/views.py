from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem

def todoView(request):
    all_todo_items = ToDoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})

# def addToDo(request):
#     new_item = ToDoItem(content=request.POST['content'])
#     new_item.save()
#     return HttpResponseRedirect('/todo/')

def addToDo(request):
    if request.method == "POST":
        new_item = ToDoItem(content = request.POST['content'])
        new_item.save()
        return HttpResponseRedirect('/todo/')
    

def deleteToDo(request, pk):
    delete_item = ToDoItem.objects.get(pk=pk)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')
