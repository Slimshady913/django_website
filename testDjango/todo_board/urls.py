from django.urls import path
from . import views

app_name = 'todo_board'
urlpatterns = [
    path('', views.todo_board_list, name='todo_board_list'),
    path('insert/', views.check_post, name='todo_board_insert'),
    path('detail/<int:pk>/', views.todo_board_detail, name='todo_board_detail'),
]

