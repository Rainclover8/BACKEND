from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name="register"),
    path('login', login, name="login"),
    path('userLogout', userLogout, name="logout"),
    path('updatePassord', update_password, name="update_password")
]
