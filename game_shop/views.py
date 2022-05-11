from re import template
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
from .models import Game
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class GameListView(ListView):
    model=Game
    context_object_name="game_list" #название списка для index.html
    template_name="games/index.html"

class GameDetailView(LoginRequiredMixin,DetailView):
    model=Game
    context_object_name="game"
    template_name="games/game.html"


#def index(request):
 #   game_list=Game.objects.all()
  #  return render(request,"games/index.html",{"game_list":game_list})
        