from django.urls import path
from .views import issue_list, issue_detail, issue_create, issue_update, issue_delete

app_name = "issues"

urlpatterns = [
    path('', issue_list, name='issue-list'),
    path('create/', issue_create, name='issue-create'),
    path('<int:pk>/', issue_detail, name='issue-detail'),
    path('<int:pk>/update/', issue_update, name='issue-update'),
    path('<int:pk>/delete/', issue_delete, name='issue-delete'),
]