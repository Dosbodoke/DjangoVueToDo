from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from API.serializers import TaskSerializer
from API.models import Task

class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'