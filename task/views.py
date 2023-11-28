# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Task
# from .serializers import TaskSerializer,WriteTaskSerializer
# from rest_framework.permissions import IsAuthenticated

# # Create your views here.

# class TaskModelViewSet(viewsets.ModelViewSet):
#     """
#         This helps Admin to create, read, update, and delete Task
#     """
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()

#     def get_permissions(self):
#         # Define permissions for each action
#         if self.action in ['list', 'retrieve','create', 'update', 'delete']:
#             # IsAuthenticated list and retrieve actions
#             permission_classes = [IsAuthenticated]
#         else:
#             # IsAuthenticated for other actions (create, update, delete)
#             permission_classes = [IsAuthenticated]
#         return [permission() for permission in permission_classes]
    
#     def get_serializer_class(self):
#         if self.action in ['list', 'retrieve']:
#             return TaskSerializer
#         return WriteTaskSerializer

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

        
        