from django.contrib import admin
from django.urls import path
from tasks_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.task_view , name='home'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle_complete'),
]




