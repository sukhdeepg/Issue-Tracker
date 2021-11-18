from django.urls import path
from .views import DeveloperListView, DeveloperCreateView, DeveloperDetailView, DeveloperUpdateView, DeveloperDeleteView

app_name = 'developers'

urlpatterns = [
    path('', DeveloperListView.as_view(), name='developer-list'),
    path('create/', DeveloperCreateView.as_view(), name='developer-create'),
    path('<int:pk>/', DeveloperDetailView.as_view(), name='developer-detail'),
    path('<int:pk>/update/', DeveloperUpdateView.as_view(), name='developer-update'),
    path('<int:pk>/delete/', DeveloperDeleteView.as_view(), name='developer-delete'),
]
