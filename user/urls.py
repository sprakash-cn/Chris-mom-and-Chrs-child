from django.urls import path,include
from user.views import dashboard

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),

]