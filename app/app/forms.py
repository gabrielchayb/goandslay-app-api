from django import forms
from core.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'birth_date', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Oculta a senha ao digitar
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Define a senha corretamente
        if commit:
            user.save()
        return user