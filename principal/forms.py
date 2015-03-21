from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("first_name","last_name","username", "email", "password1", "password2")
    def save(self, commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        email = self.cleaned_data['email']
        user.email=email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists") ##Resolver que hacer al ya existir un email
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

