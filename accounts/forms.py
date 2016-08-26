# UserCreationForm = formulário padrão que o django usa no admin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


# Esta classe será para customizar o UserCreationForm do django
# Nesse caso, herdando de UserCreationForm, pegamos toda a lógica e campos originais
# e adicionamos os nossos campos: username e email
class UserAdminCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']
