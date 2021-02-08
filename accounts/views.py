from django.shortcuts import render, redirect
from .models import Analyst, Task
from .forms import TaskForm

# Create your views here.

def home(request):
    current_analyst = request.user.analyst
    my_tasks = Task.objects.filter(assignee=current_analyst)
    print(current_analyst)
    print(my_tasks)
    context={'my_tasks':my_tasks}
    return render(request, 'accounts/dashboard.html',context)

def check(request):
    current_analyst = request.user.analyst
    my_tasks = Task.objects.filter(reporter=current_analyst)
    context={'my_tasks':my_tasks}
    return render(request, 'accounts/dashboard.html',context)

def taskDetails(request,pk):
    form = TaskForm()
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request, 'accounts/task_details.html',context) 