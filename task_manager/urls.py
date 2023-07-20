from django.urls import path
from task import views

urlpatterns = [
    path('task/', views.task_list, name='task_list'),
    path('task/calendar/', views.calendar_view, name='task_calendar'),
    path('task/get_tasks_json/', views.get_tasks_json, name='get_tasks_json'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
