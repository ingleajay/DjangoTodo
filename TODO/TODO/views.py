from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from .forms import AddTaskForm
from django.contrib import messages
from .models import AddTask

acc = None
ft = None
show = None
pi = None
def index(request):
    global acc,ft,show
    if request.user.is_authenticated:
        acc = SocialAccount.objects.get(user=request.user)
        show = AddTask.objects.all().filter(username=request.user)
        if request.method == 'POST':
            ft = AddTaskForm(request.POST)
            if ft.is_valid():
                instance = ft.save(commit=False)
                instance.username = request.user
                ft.save()
                messages.success(
                            request, ' Task Added Successfully ')
                ft = AddTaskForm()
        else:
                ft = AddTaskForm()
    return render(request, 'TODO/index.html', {'data': acc, 'form': ft,'detail':show})
    
    
def delete_task(request, id):
    if request.method == 'POST':
        pi = AddTask.objects.get(pk=id)
        pi.delete()
        print(pi)
        messages.success(
            request, 'Task Deleted Successfully ')
        return HttpResponseRedirect('/')
    return render(request, 'TODO/deletetask.html')
    
def edit_task(request, id):
    global pi
    pi = AddTask.objects.get(pk=id)
    if request.method == 'POST':
        fe = AddTaskForm(request.POST,instance=pi)
        if fe.is_valid():
            instance = fe.save(commit=False)
            instance.username = request.user
            fe.save()
            messages.success(
                request, 'Task Updated Successfully ')
        return HttpResponseRedirect('/')
    else:
        fe = AddTaskForm(instance=pi)
    return render(request, 'TODO/edit.html',{'form': fe})