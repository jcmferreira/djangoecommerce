from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import User
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):
    # Todos os add_ são para incluir opções novas do nosso User customizad
    # Aqui, é dito qual será a classe herdade de UserCreationForm utilizada pelo admin customizado
    add_form = UserAdminCreationForm
    # Aqui, serão informados os campos (fieldset) dos campos
    # É bom manter apenas os campos obrigatórios nessa primeira etapa do cadastro no admin
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    # Definindo a classe de formulário customizada para o nosso novo admin
    form = UserAdminForm
    # Definindo os grupos de campos que serão exibidos
    fieldsets = (
        (None, {
            'fields': ('username', 'email')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'last_login')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )
    # Aqui, são informados os campos que serão exibidos
    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserAdmin)
