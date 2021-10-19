from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Issue, Developer
from .forms import IssueForm

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

    form = IssueForm()

    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            developer = Developer.objects.first()
            Issue.objects.create(
                title=title,
                category='P1',
                developer=developer
            )
            return redirect("/issues")

    context = {
        "form": form
    }
    return render(request, "issues/issue_create.html", context)