from django.shortcuts import render, redirect
from .models import Task, Client
from .forms import TaskForm, ClientForm, FundForm
from .filters import TaskFilter, ClientFilter

# Create your views here.

def home(request):
    if request.method == 'GET':
        current_analyst = request.user.analyst
        my_tasks = Task.objects.filter(assignee=current_analyst)
        myFilter = TaskFilter(request.GET, queryset=my_tasks)
        my_tasks = myFilter.qs
        form = TaskForm({'assignee':current_analyst})

    if request.method == 'POST':
        current_analyst = request.user.analyst
        form = TaskForm(request.POST, {'assignee':current_analyst})
        if form.is_valid():
            new_assignee = form.save(commit=False)
            new_assignee.assignee = current_analyst
            new_assignee.save()
            form.save()
            return redirect("/")

    

    context={'my_tasks':my_tasks, 'form':form, 'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html',context)

def check(request):
    if request.method == 'GET':
        current_analyst = request.user.analyst
        my_tasks = Task.objects.filter(reporter=current_analyst)
        myFilter = TaskFilter(request.GET, queryset=my_tasks)
        my_tasks = myFilter.qs
        form = TaskForm({'reporter':current_analyst})

    if request.method == 'POST':
        current_analyst = request.user.analyst
        form = TaskForm(request.POST, {'reporter':current_analyst})
        if form.is_valid():
            new_assignee = form.save(commit=False)
            new_assignee.assignee = current_analyst
            new_assignee.save()
            form.save()
            return redirect("/")

    context={'my_tasks':my_tasks, 'form':form, 'myFilter':myFilter}
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
    clients = Client.objects.all()

    myFilter = ClientFilter(request.GET, queryset=clients)
    clients = myFilter.qs
    
    context={'clients':clients, 'myFilter':myFilter}
    return render(request, 'accounts/clients.html',context) 

def funds(request):
    funds = Funds.objects.all()
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