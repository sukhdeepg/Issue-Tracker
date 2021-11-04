from django.shortcuts import reverse
from django.core.mail import send_mail
from django.views import generic
from .models import Issue
from .forms import IssueModelForm, CustomUserCreationForm

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class IssueListView(generic.ListView):
    template_name = "issues/issue_list.html"
    queryset = Issue.objects.all()
    context_object_name = "issues"

class IssueDetailView(generic.DetailView):
    template_name = "issues/issue_detail.html"
    queryset = Issue.objects.all()
    context_object_name = "issue"

class IssueCreateView(generic.CreateView):
    template_name = "issues/issue_create.html"
    form_class = IssueModelForm

    def get_success_url(self):
        return reverse("issues:issue-list")

    def form_valid(self, form):
        send_mail(
            subject="Issue has been created",
            message="Test issue message",
            from_email="test@sukhdeep.tech",
            recipient_list=["test_recipient@sukhdeep.tech"]
        )
        return super(IssueCreateView, self).form_valid(form)

class IssueUpdateView(generic.UpdateView):
    template_name = "issues/issue_update.html"
    queryset = Issue.objects.all()
    form_class = IssueModelForm

    def get_success_url(self):
        return reverse("issues:issue-list")

class IssueDeleteView(generic.DeleteView):
    template_name = "issues/issue_delete.html"
    queryset = Issue.objects.all()

    def get_success_url(self):
        return reverse("issues:issue-list")