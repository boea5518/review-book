from cProfile import label
from attr import fields
from django import forms
from .models import Review 
# class ReviewForm(forms.Form):
#     name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={"placeholder":"Введите имя:"}),label="Имя")
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Введите почту:"}),label="Электронная почта")
#     rate=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Какой вы хотите поставить рейтинг:"}),label="Рейтинг",min_value=1,max_value=5)
#     review=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Напишите свой отзыв:"}),label="Отзыв")
class ReviewModelForm(forms.ModelForm):
    class Meta:
        model=Review 
        fields=["name","email","rate","Review"]
        widgets={
            "rate":forms.NumberInput(attrs={"placeholder":"Какой вы хотите поставить рейтинг:","min":1,"max":5}),
            "name":forms.TextInput(attrs={"placeholder":"Введите имя:"}),
            "email":forms.EmailInput(attrs={"placeholder":"Введите почту:"}),
            "Review":forms.Textarea(attrs={"placeholder":"Напишите свой отзыв:"})

        }
    