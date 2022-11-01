from django.urls import path
from accounts.views import user_login, user_logout, signup
# from projects.views import theme


urlpatterns = [
    # path('theme/', theme, name='theme'),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup, name="signup"),
]
