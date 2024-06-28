from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from myapp.forms import TodoListForm
from myapp.models import TodoList, Status

def create_item(request):
    todo = TodoList.objects.all()
    status_list = Status.objects.all()
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    form = TodoListForm()
    context = {"form": form, 'todo': todo, 'status_list': status_list}
    return render(request, 'index.html', context)

def delete_item(request):
    todo_id  = request.GET.get('todo_id')
    todo = TodoList.objects.get(id=todo_id)
    todo.delete()
    data = {'status':'delete'}
    return JsonResponse(data)

def update_item(request):
    data_id = request.GET.get('data_id')
    title = request.GET.get('title')
    print(data_id, title)

    todo = get_object_or_404(TodoList, id=data_id)
    todo.title = title
    todo.save()

    data = {'status': 'update-item', 'title':title}
    return JsonResponse(data)

def update_status(request):  
    data_id  = request.GET.get('data_id')
    status_id = request.GET.get('status_id')

    status = Status.objects.get(id=status_id) 
    
    todo = get_object_or_404(TodoList,id=data_id)
    todo.status = status
    todo.save()
    
    data = {'status':status_id}
    return JsonResponse(data)
