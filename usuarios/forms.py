from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UsuarioCustom


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = UsuarioCustom
        fields = {'first_name', 'last_name', 'cpf'}
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']

        if commit:
            user.save()
        return user


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioCustom
        fields = {'first_name', 'last_name', 'cpf'}

