from django.urls import path , include
from login import views

urlpatterns = [
    path('', views.login),
    path('success', views.logout),
]