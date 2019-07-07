from django.urls import path
from . import views

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('/hello2', views.hello2, name='hello2'),
    path('/hello3', views.hello3, name='hello3'),
]