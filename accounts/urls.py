from django.urls import path
import django.contrib.auth.views as auth_views

urlpatterns=[
    path("login/",auth_views.LoginView.as_view(),name="login"),  #1.Адрес 2.обработчик 3.имя мршрута
    path("logout/",auth_views.LogoutView.as_view(),name="logout")
]