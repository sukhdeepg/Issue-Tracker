from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView, AssignDeveloperView, CategoryListView, CategoryDetailView, IssueCategoryUpdateView

app_name = "issues"

urlpatterns = [
    path('', IssueListView.as_view(), name='issue-list'),
    path('create/', IssueCreateView.as_view(), name='issue-create'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),
    path('<int:pk>/update/', IssueUpdateView.as_view(), name='issue-update'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='issue-delete'),
    path('<int:pk>/assign_developer/', AssignDeveloperView.as_view(), name='assign-developer'),
    path('<int:pk>/category/', IssueCategoryUpdateView.as_view(), name='issue-category-update'),
    path('categories', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail')
]