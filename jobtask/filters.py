import django_filters
from django import forms
from .models import Job, JOB_TYPES

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search Job Title',
        })
    )
    location = django_filters.CharFilter(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Preferred Location',
        })
    )
    type = django_filters.ChoiceFilter(
        choices=JOB_TYPES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Select Job Type',
        })
    )
    salary_min = django_filters.NumberFilter(
        field_name='salary_min',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min Salary',
        })
    )
    salary_max = django_filters.NumberFilter(
        field_name='salary_max',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Max Salary',
        })
    )

    class Meta:
        model = Job
        fields = ['title', 'location', 'type', 'salary_min', 'salary_max']
