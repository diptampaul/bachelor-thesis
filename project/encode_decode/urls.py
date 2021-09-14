from django.urls import path
from . import views


urlpatterns = [
    path('',views.ecdc, name='ecdc'),
    path('decode', views.decode, name='decode')
]