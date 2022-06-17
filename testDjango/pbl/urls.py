from django.urls import path
from . import views

app_name = 'pbl'
urlpatterns = [
    path('', views.pbl, name='pbl')
]