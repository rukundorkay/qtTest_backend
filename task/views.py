from rest_framework import generics
from .models import Task,Assignees
from .serializers import TaskSerializer,AssignesSerializer
from rest_framework.permissions import IsAuthenticated

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssigneeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Assignees.objects.all()
    serializer_class = AssignesSerializer


class AssigneeCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Assignees.objects.all()
    serializer_class = AssignesSerializer

        
        