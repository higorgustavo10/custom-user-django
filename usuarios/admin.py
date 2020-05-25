from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UsuarioCustom
from .forms import UsuarioCreateForm, UsuarioChangeForm



@admin.register(UsuarioCustom)
class UsuarioCustomAdmin(UserAdmin):
    add_form = UsuarioCreateForm
    form = UsuarioChangeForm
    model = UsuarioCustom
    list_display = ('first_name', 'last_name', 'email', 'cpf', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'cpf')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined',)}),
    )
