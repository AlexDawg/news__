import django_filters
from django import forms
from django_filters import FilterSet
from .models import Post, Category
from django.forms.widgets import DateInput, CheckboxSelectMultiple


class PostFilter(FilterSet):
    title = django_filters.Filter(field_name='title', lookup_expr='icontains')
    time_in = django_filters.DateFilter(field_name='time_in', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}))
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'categories': 'postcategory'}), label='Category')
    class Meta:
        model = Post
        fields = [
            'title',
            'time_in',
            'categories',
        ]
