from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('give/',views.attendance, name='attendance'),
]