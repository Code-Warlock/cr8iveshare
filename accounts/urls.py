from django.urls import path
from .views import *
from accounts.views import *


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout_user/', logout_view, name='logout_user'),
    path('forgot_pass/', forgot_password, name='forgot_password'),
]
