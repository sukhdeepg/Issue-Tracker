from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Issue

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}

class IssueModelForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            'title',
            'category',
            'team',
            'developer'
        )