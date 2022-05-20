from django.urls import path
import django.contrib.auth.views as auth_views
from .views import UserCreationView

urlpatterns=[
    path("login/",auth_views.LoginView.as_view(),name="login"),  #1.Адрес 2.обработчик 3.имя мршрута
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
    path("reg/",UserCreationView.as_view(),name="reg"),
    path("password_change/",auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password_change_done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done")
]