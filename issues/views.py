from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.views import generic
from .models import Issue, UserProfile
from .forms import IssueModelForm, CustomUserCreationForm
from developers.mixins import OwnerAndLoginRequiredMixin

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

class IssueListView(LoginRequiredMixin, generic.ListView):
    template_name = "issues/issue_list.html"
    context_object_name = "issues"
    
    def get_queryset(self):
        user = self.request.user

        if user.is_owner:
            queryset = Issue.objects.filter(team=user.userprofile, 
                developer__isnull=False
            )
        else:
            queryset = Issue.objects.filter(team=user.developer.team)
            queryset = queryset.filter(developer__user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        user = self.request.user
        
        if user.is_owner:
            queryset = Issue.objects.filter(
                team=user.userprofile,
                developer__isnull=True
            )
            context.update({
                "unassigned_issues": queryset
            })
        return context

class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "issues/issue_detail.html"
    context_object_name = "issue"

    def get_queryset(self):
        user = self.request.user

        if user.is_owner:
            queryset = Issue.objects.filter(team=user.userprofile)
        else:
            queryset = Issue.objects.filter(team=user.developer.team)
            queryset = queryset.filter(developer__user=self.request.user)

        return queryset

class IssueCreateView(OwnerAndLoginRequiredMixin, generic.CreateView):
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

class IssueUpdateView(OwnerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "issues/issue_update.html"
    form_class = IssueModelForm

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(team=user.userprofile)

    def get_success_url(self):
        return reverse("issues:issue-list")

class IssueDeleteView(OwnerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "issues/issue_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(team=user.userprofile)

    def get_success_url(self):
        return reverse("issues:issue-list")