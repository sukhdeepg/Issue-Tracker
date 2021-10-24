from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Issue, Developer
from .forms import IssueModelForm

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

def issue_create(request):

    form = IssueModelForm()

    if request.method == "POST":
        form = IssueModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/issues")

    context = {
        "form": form
    }
    return render(request, "issues/issue_create.html", context)

def issue_update(request, pk):
    issue = Issue.objects.get(id=pk)

    form = IssueModelForm(instance=issue) 

    if request.method == "POST":
        form = IssueModelForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect("/issues")

    context = {
        "form": form,
        "issue": issue
    }
    return render(request, "issues/issue_update.html", context)

def issue_delete(request, pk):
    issue = Issue.objects.get(id=pk)
    issue.delete()

    return redirect("/issues")