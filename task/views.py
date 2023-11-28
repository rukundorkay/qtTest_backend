

import datetime
from .models import Task,Assignees
from .serializers import TaskSerializer,AssignesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AssigneeDetailView(generics.RetrieveUpdateDestroyAPIView):
    # swagger_schema = None
    permission_classes = [IsAuthenticated]
    queryset = Assignees.objects.all()
    serializer_class = AssignesSerializer


class AssigneeCreateView(generics.ListCreateAPIView):
    # swagger_schema = None
    permission_classes = [IsAuthenticated]
    queryset = Assignees.objects.all()
    serializer_class = AssignesSerializer

class Analytics(APIView):
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        total= Task.objects.count()
        today= Task.objects.filter(created_at=datetime.date.today()).count()
        weekly= Task.objects.filter(created_at=datetime.date.today()).count()
        monthly= Task.objects.filter(created_at=datetime.date.today()).count()
        return Response({
                'total':total,
                'today':today,
                'monthly':monthly,
                'weekly':weekly,
                
            }, status=status.HTTP_200_OK)
    



        
        