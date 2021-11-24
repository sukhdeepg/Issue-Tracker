from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.models import ModelChoiceField
from django.http import request

from .models import Issue, Developer

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

class AssignDeveloperForm(forms.Form):
    developer = ModelChoiceField(queryset=Developer.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        developers = Developer.objects.filter(team=request.user.userprofile)
        super(AssignDeveloperForm, self).__init__(*args, **kwargs)
        self.fields["developer"].queryset = developers

class IssueCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = (
            'category',
        )