from django.urls import path
from .views import TaskListCreateView, TaskDetailView,AssigneeCreateView,AssigneeDetailView,Analytics

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<str:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('assignees',AssigneeCreateView.as_view(),name='assignee-list-create'),
    path('assignees/<str:pk>/',AssigneeDetailView.as_view(),name='assignee-details'),
    path('analytics',Analytics.as_view(),name='analytics'),

]