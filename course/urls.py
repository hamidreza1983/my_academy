from django.urls import path
from .views import *



app_name = 'course'

urlpatterns = [
    path('', course, name='course'),
    path('detail/<int:pid>', course_detail, name='course_detail'),
]
