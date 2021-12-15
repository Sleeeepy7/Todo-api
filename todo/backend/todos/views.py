from rest_framework import generics
from .models import Todo
from .serializers import ToDoSerializer


class ListToDo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer


class DetailToDo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
