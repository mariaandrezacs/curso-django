from django.urls import path

from . import views


# HTTP REQUEST <- HTTP RESPONSE

urlpatterns = [
    path('', views.home), 
    path('recipes/<int:id>/', views.recipe), 
    

]