import random

from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from issues.models import Developer
from .forms import DeveloperModelForm
from .mixins import OwnerAndLoginRequiredMixin

class DeveloperListView(OwnerAndLoginRequiredMixin, generic.ListView):
    template_name = "developers/developer_list.html"

    def get_queryset(self):
        team = self.request.user.userprofile
        return Developer.objects.filter(team=team)

class DeveloperCreateView(OwnerAndLoginRequiredMixin, generic.CreateView):
    template_name = "developers/developer_create.html"
    form_class = DeveloperModelForm

    def get_success_url(self):
        return reverse("developers:developer-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_owner = False
        user.save()
        Developer.objects.create(
            user=user,
            team=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be a developer",
            message="Please login to start working with Issue Tracker.",
            from_email="admin@sukhdeep.tech",
            recipient_list=[user.email]
        )
        return super(DeveloperCreateView, self).form_valid(form)

class DeveloperDetailView(OwnerAndLoginRequiredMixin, generic.DetailView):
    template_name = "developers/developer_detail.html"
    context_object_name = "developer"

    def get_queryset(self):
        team = self.request.user.userprofile
        return Developer.objects.filter(team=team)

class DeveloperUpdateView(OwnerAndLoginRequiredMixin, generic.UpdateView):
    template_name = "developers/developer_update.html"
    form_class = DeveloperModelForm

    def get_success_url(self):
        return reverse("developers:developer-list")

    def get_queryset(self):
        team = self.request.user.userprofile
        return Developer.objects.filter(team=team)

class DeveloperDeleteView(OwnerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "developers/developer_delete.html"
    context_object_name = "developer"

    def get_success_url(self):
        return reverse("developers:developer-list")

    def get_queryset(self):
        team = self.request.user.userprofile
        return Developer.objects.filter(team=team)
