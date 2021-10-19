from django.urls import path
from .views import issue_list, issue_detail, issue_create

app_name = "issues"

urlpatterns = [
    path('', issue_list),
    path('create/', issue_create),
    path('<int:pk>/', issue_detail)
]