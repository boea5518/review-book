from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserSingUpForm

# Create your views here.
class UserCreationView(CreateView):
    form_class=UserSingUpForm
    success_url=reverse_lazy("login")  #revers для классов (по имеи марщрута проходит по маршруту)
    template_name="accounts/sign_up.html"
    