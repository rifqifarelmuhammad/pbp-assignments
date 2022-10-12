from django.urls import path
from todolist.views import delete_task, register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import update
from todolist.views import delete
from todolist.views import return_data_JSON
from todolist.views import add_task
from todolist.views import delete_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('update/<update_id>', update, name='update'),
    path('delete/<delete_id>', delete_task, name='delete_task'),
    path('json/', return_data_JSON, name='return_data_JSON'),
    path('add/', add_task, name='add_task'),
]