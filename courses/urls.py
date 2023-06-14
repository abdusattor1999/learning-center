from django.urls import path, include
from .views import *

app_name = 'courses'
urlpatterns = [
    path('courses/<int:pk>/', course_details , name='details'),
    path('teacher/', teacher , name='teacher_list'),
    path('teacher/<int:pk>/', teacher , name='teacher'),
    path('', home , name='home'),
]


