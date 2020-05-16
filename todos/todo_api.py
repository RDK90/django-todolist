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
