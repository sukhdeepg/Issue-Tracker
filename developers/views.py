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