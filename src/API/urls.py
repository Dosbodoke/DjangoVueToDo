from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView

app_name = "API"
urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list'), 
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy'),
    ]