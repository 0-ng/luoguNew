from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=20)
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput)