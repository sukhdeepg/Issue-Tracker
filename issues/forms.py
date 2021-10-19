from django import forms

class IssueForm(forms.Form):
    title = forms.CharField()
    