from cProfile import label
from django import forms
class ReviewForm(forms.Form):
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={"placeholder":"Введите имя:"}),label="Имя")
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Введите почту:"}),label="Электронная почта")
    review=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Напишите свой отзыв:"}),label="Отзыв")