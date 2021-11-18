from django.contrib.auth.models import update_last_login
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
        developer = form.save(commit=False)
        developer.team = self.request.user.userprofile
        developer.save()
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
