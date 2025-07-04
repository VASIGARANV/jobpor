from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Job
        fields = "__all__"
