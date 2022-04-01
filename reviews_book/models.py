import email
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Review(models.Model):
    def __str__(self):
        return self.email
    name=models.CharField(max_length=25,verbose_name="Имя пользователя")
    email=models.EmailField(verbose_name="Почта пользователя")
    rate=models.IntegerField(verbose_name="Рейтинг",validators=[MinValueValidator(1),MaxValueValidator(5)])
    Review=models.TextField(verbose_name="Отзыв")
    class Meta:
        verbose_name_plural="Отзывы"

