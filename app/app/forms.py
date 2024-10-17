from django import forms
from core.models import User
from django.contrib.auth import authenticate , get_user_model

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
    


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput()) 


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'birth_date']
