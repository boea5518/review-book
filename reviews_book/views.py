import email
from webbrowser import get
from django.shortcuts import redirect, render
from .forms import ReviewForm

# Create your views here.
def reviews(request):
    if request.method=="GET":
        form=ReviewForm()
        return render (request,"reviews.html",{"form":form})
    elif request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get("name")
            email=data.get("email")
            review=data.get("review")
            with open("review.csv",mode="a",encoding="UTF-8") as file:
                file.write(f"{name}|{email}|{review}\n")
            return redirect("reviews")
        else:
            form=ReviewForm()
        # name=request.GET.get("name")
        # email=request.GET.get("email")
        # review=request.GET.get("review")
            return render (request,"reviews.html",{"form":form})