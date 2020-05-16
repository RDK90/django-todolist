from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET', 'POST'])
def get_all_todos(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data)
    elif request.method == "POST":
        if "title" in request.data[0] and "text" in request.data[0]:
            data = {
                "title":request.data[0]['title'],
                "text":request.data[0]['text']
            }
        else:
            content = "{} is an invalid payload".format(request.data[0])
            return Response(content, status=status.HTTP_400_BAD_REQUEST)        
        todo_serializer = TodoSerializer(data=data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = "{} is not a valid payload".format(request.data)
            return Response(content, status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def todos_by_id(request, todo_id):
    try:
        todo_id = int(todo_id)
    except:
        content = {"{} is an invalid ID".format(todo_id)}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
    todos = Todo.objects.filter(id=todo_id).values()
    if not todos:
        content = {"Todo item with ID {} not found".format(todo_id)}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data)
    elif request.method == "PUT":
        data = request.data
        todo_serializer = TodoSerializer(data=data, many=True)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return Response(todo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = "{} is not a valid payload".format(request.data)
            return Response(content, status.HTTP_400_BAD_REQUEST)
    

