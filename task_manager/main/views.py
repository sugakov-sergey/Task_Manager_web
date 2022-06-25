from django.shortcuts import render, redirect

from .forms import TaskForm, PurposeForm
from .models import Task

def index(request):
    tasks = Task.objects.order_by('-id')
    context = {
        'title': 'Главная страница',
        'tasks': tasks
               }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Введены неверные данные'
    form = TaskForm()
    context = {'form': form,
               'error': error}
    return render(request, 'main/create.html', context)


def purpose(request):
    form = PurposeForm()
    context = {'form': form}
    return render(request, 'main/purpose.html', context)