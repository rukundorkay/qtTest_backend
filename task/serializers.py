from rest_framework import serializers
from .models import Task,Assignees

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
class AssignesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignees
        fields ='__all__'