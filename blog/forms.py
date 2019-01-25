from django import forms


class BlogEntry(forms.Form):
    blogTitle = forms.CharField()
    blogTags = forms.CharField()
    blogContent = forms.CharField()
