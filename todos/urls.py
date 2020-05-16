from django.urls import path

from . import views, todo_api

app_name = "todos"

urlpatterns = [
    path('todos/', views.index, name='index'),
    path('todos/all', todo_api.get_all_todos, name="get_all_todos"),
    path('todos/<todo_id>', todo_api.todos_by_id, name="todo_by_id"),
    path('details/<id>', views.details),
    path('add/', views.add, name='add')
]
