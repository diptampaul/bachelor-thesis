from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('students',views.students, name='students'),
    path('faculty',views.faculty, name='faculty'),
]