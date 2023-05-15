from django.urls import path
from . import views
from views import Login
urlpatterns = [
    path('', views.getData),
    path('login/', Login.as_view(), name="login")
]