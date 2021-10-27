from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from issues.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('issues/', include('issues.urls', namespace="issues")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)