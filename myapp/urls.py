from django.urls import path
from .views import register_user, login_user, google_login, stats

urlpatterns = [
    path("register/", register_user),
    path("login/", login_user),
    path("google-login/", google_login),   # ✅ NEW
    path("stats/", stats),                 # ✅ OPTIONAL
]