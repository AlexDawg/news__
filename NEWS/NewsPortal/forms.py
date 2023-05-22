from django import forms
from django.core.exceptions import ValidationError

from .models import Post, PostCategory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'author',
            'categories',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get('title')

        if title == text:
            raise ValidationError(
                "Текст должен отличаться от названия"
            )
        return cleaned_data


