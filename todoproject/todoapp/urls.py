from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),

    path('gvhome/', views.TaskListview.as_view(), name='gvhome'),
    path('gvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='gvdetail'),
    path('gvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='gvupdate'),
    path('gvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='gvdelete'),
]