from django.shortcuts import render, redirect
from .models import Analyst, Task
from .forms import TaskForm, ClientForm, FundForm

# Create your views here.

def home(request):
    current_analyst = request.user.analyst
    my_tasks = Task.objects.filter(assignee=current_analyst)
    print(current_analyst)
    print(my_tasks)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = TaskForm(request.POST,)
            form.save()
            return redirect("/")

    context={'my_tasks':my_tasks, 'form':form}
    return render(request, 'accounts/dashboard.html',context)

def check(request):
    current_analyst = request.user.analyst
    my_tasks = Task.objects.filter(reporter=current_analyst)
    context={'my_tasks':my_tasks}
    return render(request, 'accounts/dashboard.html',context)

def updateTask(request,pk):
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

def clients(request):
    clients = Client.objects.get.all()
    context={'clients':clients}
    return render(request, 'accounts/task_details.html',context) 

def funds(request):
    funds = Funds.objects.get.all()
    context={'funds':funds}
    return render(request, 'accounts/task_details.html',context) 

def updateClient(request,pk):
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

def updateFund(request,pk):
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