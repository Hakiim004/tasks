from django.shortcuts import redirect, render , get_object_or_404

from tasks_app.models import Task
from .forms import task_appForm
# Create your views here.

def task_view(request):
    if request.method == 'POST':
        form = task_appForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = task_appForm()
    tasks = Task.objects.all().order_by('-created_at')
    context = {'form':form ,
               'tasks':tasks ,
    }
    return render(request, 'home.html' , context)


def update_task(request , pk):
    tasks = get_object_or_404(Task  , pk = pk  )
    form = task_appForm(request.POST or None , instance= tasks)
     if form.is_valid():
        form.save()

    return     redirect('home')
    return render(request , 'update.html' ,{'form':form})

def delete_task(request , pk):
    tasks = get_object_or_404(Task , pk=pk)
    if request.method =='POST':
        tasks.delete()
        redirect('home')
    return render(request , "delete.html", {'tasks':tasks })


def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('home')
