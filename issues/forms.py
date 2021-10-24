from django import forms
from .models import Issue

class IssueModelForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            'title',
            'category',
            'developer'
        )