from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue

def home_page(request):
    issues = Issue.objects.all()
    context = {
        "issues": issues
    }
    return render(request, "second_page.html", context)