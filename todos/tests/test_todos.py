import json

from django.test import TestCase
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import status
from rest_framework.test import APIClient

from todos.models import Todo
from todos.serializers import TodoSerializer

class TestTodos(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.first_todo = Todo.objects.create(title="test", text="test again")
        self.second_todo = Todo.objects.create(title="test2", text="test data")
        self.valid_payload = [{
            "title":"valid_payload", 
            "text":"valid_payload text",
        }]
        self.invalid_payload = [{
            "title":"", 
            "text":"valid_payload text",
        }]

    def test_get_all_todos(self):
        response = self.client.get(reverse('todos:get_all_todos'))
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo_serializer.data[0]['id'], response.data[0]['id'])

    def test_get_todo_by_id(self):
        test_id = self.first_todo.id
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

    def test_put_todo_by_id(self):
        response = self.client.put(
            reverse('todos:todo_by_id', kwargs={'todo_id':self.first_todo.id}),
            data=json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_invalid_todo_by_id(self):
        response = self.client.put(
            reverse('todos:todo_by_id', kwargs={'todo_id':self.first_todo.id}),
            data=json.dumps(self.invalid_payload, cls=DjangoJSONEncoder),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_todo_by_unknown_id(self):
        response = self.client.put(
            reverse('todos:todo_by_id', kwargs={'todo_id':656434618346873737}),
            data=json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_todo_by_invalid_id(self):
        response = self.client.put(
            reverse('todos:todo_by_id', kwargs={'todo_id':"foireuifoif"}),
            data=json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
