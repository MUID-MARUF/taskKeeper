from django.urls import path 
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.registerUser, name = 'create user'),
    path('',  views.getTasks, name = 'tasks'),
    path('create/', views.createTask, name = 'create task'),
    path('update/<uuid:pk>/', views.updateTask, name = 'update task'),
    path('delete/<uuid:pk>/', views.deleteTask, name = 'delete task'),
]
