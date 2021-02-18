from django.shortcuts import render, redirect, HttpResponse

from .models import Task, Client, Fund
from .forms import TaskForm, ClientForm, FundForm
from .filters import TaskFilter, ClientFilter, FundFilter

def home(request):
    current_analyst = request.user.analyst
    title = 'What do I have to do today?'

    if request.method == 'GET':
        my_tasks = Task.objects.filter(assignee=current_analyst)
        myFilter = TaskFilter(request.GET, queryset=my_tasks)
        my_tasks = myFilter.qs.order_by('-date_created')
        form = TaskForm({'assignee':current_analyst})
        

    if request.method == 'POST':
        form = TaskForm(request.POST, {'assignee':current_analyst})
        if form.is_valid():
            new_assignee = form.save(commit=False)
            new_assignee.assignee = current_analyst
            new_assignee.save()
            form.save()
            return redirect("/")

    context={'title':title, 'my_tasks':my_tasks, 'form':form, 'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html',context)


def check(request):
    current_analyst = request.user.analyst
    title = 'What to I have to check today?'

    if request.method == 'GET':
        my_tasks = Task.objects.filter(reporter=current_analyst)
        myFilter = TaskFilter(request.GET, queryset=my_tasks)
        my_tasks = myFilter.qs
        form = TaskForm({'assignee':current_analyst})

    if request.method == 'POST':
        form = TaskForm(request.POST, {'assignee':current_analyst})
        if form.is_valid():
            new_assignee = form.save(commit=False)
            new_assignee.assignee = current_analyst
            new_assignee.save()
            form.save()
            return redirect("/")

    context={'title':title,'my_tasks':my_tasks, 'form':form, 'myFilter':myFilter}
    return render(request, 'accounts/dashboard.html',context)


def clients(request):
    title = 'Clients'
    if request.method == 'GET':
        clients = Client.objects.all()
        myFilter = ClientFilter(request.GET, queryset=clients)
        clients = myFilter.qs
        form = ClientForm

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/clients/")
    
    context={'title': title,'clients':clients, 'form':form,  'myFilter':myFilter}
    return render(request, 'accounts/clients.html',context) 


def funds(request):
    title = 'Funds'
    if request.method == 'GET':
        funds = Fund.objects.all()
        myFilter = FundFilter(request.GET, queryset=funds)
        funds = myFilter.qs
        form = FundForm
    
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/funds/")

    context={'title': title,'funds':funds, 'form':form, 'myFilter':myFilter}
    return render(request, 'accounts/funds.html',context)


def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'GET':
        form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context={'form':form}
    return render(request, 'accounts/details.html',context)



def updateClient(request,pk):
    client = Client.objects.get(id=pk)
    if request.method == 'GET':
        form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form = ClientForm(request.POST, instance=client)
            form.save()
            return redirect("clients")
    context={'form':form}
    return render(request, 'accounts/details.html',context) 


def updateFund(request,pk):
    fund = Fund.objects.get(id=pk)
    if request.method == 'GET':
        form = FundForm(instance=fund)
        
    if request.method == 'POST':
        form = FundForm(request.POST)
        if form.is_valid():
            form = FundForm(request.POST, instance=fund)
            form.save()
            return redirect("funds")
    context={'form':form}
    return render(request, 'accounts/details.html',context) 


def deleteTask(request,pk):
    if request.method == 'GET':
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect ('/')
    return HttpResponse('error: could not delete task: '+task.id)


def deleteClient(request,pk):
    if request.method == 'GET':
        client = Client.objects.get(id=pk)
        client.delete()
        return redirect ('clients')
    return HttpResponse('error: could not delete client: '+client.id)


def deleteFund(request,pk):
    if request.method == 'GET':
        fund = Fund.objects.get(id=pk)
        fund.delete()
        return redirect ('fund')
    return HttpResponse('error: could not delete fund: '+fund.id)