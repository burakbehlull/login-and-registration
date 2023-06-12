from django.urls import path
from . import views
from .views import RegisterView, UserBlogsAPIView, BlogListAPIView

from .views import LoginView
urlpatterns = [
    path('', views.getData),
    path('add/', views.AddItems),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]

