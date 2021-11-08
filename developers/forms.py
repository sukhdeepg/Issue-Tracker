from django import forms
from issues.models import Developer

class DeveloperModelForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = {
            'user',
        }