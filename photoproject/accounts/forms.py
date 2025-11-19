from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    model = CustomUser
    fielde = ('username', 'email', 'password', 'password2')