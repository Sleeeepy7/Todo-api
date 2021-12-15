from django.urls import path
from .views import ListToDo, DetailToDo

urlpatterns = [
    path('<int:pk>/', DetailToDo.as_view()),
    path('', ListToDo.as_view()),
]