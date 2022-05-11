from django.urls import path
from game_shop.views import GameListView,GameDetailView

urlpatterns=[
    path("",GameListView.as_view(),name="home"),
    path("<slug:slug>",GameDetailView.as_view(),name="game_detail")

]