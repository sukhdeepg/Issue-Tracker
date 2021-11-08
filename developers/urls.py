from django.urls import path
from .views import DeveloperListView, DeveloperCreateView

app_name = 'developers'

urlpatterns = [
    path('', DeveloperListView.as_view(), name='developer-list'),
    path('create/', DeveloperCreateView.as_view(), name='developer-create'),
]
