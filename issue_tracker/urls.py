from django.contrib import admin
from django.urls import path, include
from issues.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('issues/', include('issues.urls', namespace="issues"))
]