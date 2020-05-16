from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def get_all_todos(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data)

@api_view(['GET'])
def todos_by_id(request, todo_id):
    if request.method == "GET":
        try:
            todo_id = int(todo_id)
            todos = Todo.objects.filter(id=todo_id).values()
            if not todos:
                content = {"Todo item with ID {} not found".format(todo_id)}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            todo_serializer = TodoSerializer(todos, many=True)
            return Response(todo_serializer.data)
        except:
            content = {"{} is an invalid ID".format(todo_id)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
