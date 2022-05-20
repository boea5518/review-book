from django.db import models
from django.forms import CharField, DateTimeField
from django.contrib.auth import get_user_model
from django.urls import reverse  #url-ищет по названию маршрута
from embed_video.fields import EmbedVideoField

# Create your models here.
class Game(models.Model):
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("game_detail",args=[self.slug])

    title=models.CharField(max_length=40)
    tags=models.CharField(max_length=25)
    description=models.TextField()
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    image=models.ImageField(blank=True)
    video = EmbedVideoField(blank=True, verbose_name='Видео')

