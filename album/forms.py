from django import forms


class NewTask(forms.Form):
    title = forms.CharField()
    detail = forms.CharField(widget=forms.Textarea)
