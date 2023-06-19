from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoForm

def TodoIndex(request):
    search = request.GET.get('search', '').capitalize()
    todos = Todo.objects.filter(title__contains=search)
    context = {
        'todos': todos
    }
    return render(request, '../templates/todo/index.html', context)

def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request, '../templates/todo/detail.html', context)

def edit(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "GET":
        form = TodoForm(instance = todo)
        context = {
            'form': form,
            'id': id,
        }
        return render(request, '../templates/todo/edit.html', context)
    if request.method == "POST":
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea modificada')
            return redirect('todoIndex')
        else:
            messages.success(request, 'Ocurrio un error')
            return redirect('todoIndex')    
    
def create(request):
    if request.method == "GET":
        form = TodoForm()
        context = {
            'form': form,
        }
        return render(request, '../templates/todo/create.html', context)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea agregada')
            return redirect('todoIndex')
        else:
            messages.success(request, 'Ocurrio un error')
            return redirect('todoIndex')
        
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todoIndex')