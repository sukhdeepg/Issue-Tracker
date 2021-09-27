from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue

def issue_list(request):
    issues = Issue.objects.all()
    context = {
        "issues": issues
    }
    return render(request, "issues/issue_list.html", context)

def issue_detail(request, pk):
    issue = Issue.objects.get(id=pk)
    context = {
        "issue": issue
    }
    return render(request, "issues/issue_detail.html", context)