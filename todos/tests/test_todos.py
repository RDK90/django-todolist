import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from todos.models import Todo
from todos.serializers import TodoSerializer

class TestTodos(TestCase):

    def setUp(self):
        self.client = APIClient()
        Todo.objects.create(id=1, title="test", text="test again")
        Todo.objects.create(id=2, title="test2", text="test data")

    def test_get_all_todos(self):
        response = self.client.get(reverse('todos:get_all_todos'))
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo_serializer.data[0]['id'], response.data[0]['id'])

    def test_get_todo_by_id(self):
        test_id = 1
        response = self.client.get(reverse('todos:todo_by_id', kwargs={'todo_id':test_id}))
        todos = Todo.objects.filter(id=test_id)
        todo_serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo_serializer.data[0]['id'], response.data[0]['id'])

    def test_get_todo_by_unknown_id(self):
        test_id = 3
        response = self.client.get(reverse('todos:todo_by_id', kwargs={'todo_id':test_id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_todo_by_invalid_id(self):
        test_id = "doiebfewaf"
        response = self.client.get(reverse('todos:todo_by_id', kwargs={'todo_id':test_id}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        Todo.objects.filter(id=1).delete()
        Todo.objects.filter(id=2).delete()
