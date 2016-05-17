__author__ = 'Robin'
# _*_ coding: utf-8 _*_

from django import forms
from .models import RegisterModel, LoginModel


class RegisterForm(forms.ModelForm):
    # passw = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = RegisterModel
        widgets = {
            'passw': forms.PasswordInput(),
            'passw2': forms.PasswordInput()
        }

        fields = ('login', 'name', 'surname', 'email', 'passw', 'passw2')
        fields_required = ['login']

    # def clean_password2(self):
    #     password1 = self.cleaned_data['passw']
    #     password2 = self.cleaned_data['passw2']
    #     if password1 == password2:
    #         return password2
    #     else:
    #         raise forms.ValidationError("Hasła się różnią")
    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not re.search(r'^\w+$',username):
    #         raise forms.ValidationError("Dopuszczalne są tylko cyfry, litery angielskie i _")
    #     try:
    #         User.objects.get(username=username)
    #     except ObjectDoesNotExist:
    #         return username
    #     raise forms.ValidationError("Taki użytkownik już istnieje")

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ('login', 'password')
