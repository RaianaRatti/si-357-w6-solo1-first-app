# mysite/mysite/urls.py from DJ4E

from django.contrib import admin
from django.urls import include, path

# Redirects different URL starters to respective files
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("solo1/", include("solo1.urls")),
    path("admin/", admin.site.urls),
]