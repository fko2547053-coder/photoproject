from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2')