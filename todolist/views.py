import datetime
from todolist.models import Task
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from todolist.forms import CreateTask

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()

    data_task = Task.objects.filter(user=request.user)

    context = {
        'username': username,
        'list_task': data_task,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTask()

    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            date = datetime.datetime.now()
            title = request.POST.get('title')
            description = request.POST.get('description')
            user = request.user
            task = Task(user=user, date=date, title = title, description = description)
            task.save()
            return redirect('todolist:show_todolist')

    username = None
    if request.user.is_authenticated:
        username = request.user.get_username()

    context = {
        'form':form,
        'username': username
    }
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
def update(request, update_id):
    task_update = Task.objects.get(id=update_id)

    if task_update.is_finished == False:
        task_update.is_finished = True
    else:
        task_update.is_finished = False

    task_update.save()

    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete(request, delete_id):
    Task.objects.filter(id=delete_id).delete()
    return redirect('todolist:show_todolist')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response