from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('post/<str:blog>/', views.post_detail, name='post_detail'),
]
