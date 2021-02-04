from django.shortcuts import render
from .models import Analyst, Task

# Create your views here.

def home(request):
    current_analyst = request.user.analyst
    my_tasks = Task.objects.filter(assignee=current_analyst)
    print(current_analyst)
    print(my_tasks)
    context={'my_tasks':my_tasks}
    return render(request, 'accounts/dashboard.html',context)
