from django.urls import path

from . import views, todo_api

urlpatterns = [
    path('todos/', views.index, name='index'),
    path('todos/all', todo_api.get_all_todos, name="get_all_todos"),
    path('details/<id>', views.details),
    path('add/', views.add, name='add')
]
