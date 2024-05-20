from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("status", "created_on", "updated_on")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control content"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "author": forms.HiddenInput(),
        }
