from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path("", Login, name="login"),
    path("signup/", Signup, name="signup"),
    path("logout/", Logout, name="logout"),
]