from django import forms


class RegisterUser(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()


class Extra(forms.Form):
    name = forms.CharField()
    username = forms.CharField()


class login_main(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
