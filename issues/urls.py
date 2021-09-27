from django.urls import path
from .views import issue_list, issue_detail

app_name = "issues"

urlpatterns = [
    path('', issue_list),
    path('<pk>/', issue_detail)
]