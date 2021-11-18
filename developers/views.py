from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from issues.models import Developer
from .forms import DeveloperModelForm

class DeveloperListView(LoginRequiredMixin, generic.ListView):
    template_name = "developers/developer_list.html"

    def get_queryset(self):
        return Developer.objects.all()

class DeveloperCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "developers/developer_create.html"
    form_class = DeveloperModelForm

    def get_success_url(self):
        return reverse("developers:developer-list")

    def form_valid(self, form):
        developer = form.save(commit=False)
        developer.team = self.request.user.userprofile
        developer.save()
        return super(DeveloperCreateView, self).form_valid(form)

class DeveloperDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "developers/developer_detail.html"
    context_object_name = "developer"

    def get_queryset(self):
        return Developer.objects.all()

class DeveloperUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "developers/developer_update.html"
    form_class = DeveloperModelForm

    def get_success_url(self):
        return reverse("developers:developer-list")

    def get_queryset(self):
        return Developer.objects.all()

class DeveloperDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "developers/developer_delete.html"
    context_object_name = "developer"

    def get_success_url(self):
        return reverse("developers:developer-list")

    def get_queryset(self):
        return Developer.objects.all()