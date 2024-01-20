from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm



# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos})

def todo_list2(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/index copy.html', {'todos': todos})

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todolist/todo_form.html', {'form': form})