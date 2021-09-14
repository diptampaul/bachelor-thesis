from django.urls import path
from . import views


urlpatterns = [
    path('',views.ecdc, name='ecdc'),
]