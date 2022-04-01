import email
from webbrowser import get
from django.shortcuts import redirect, render
from .forms import ReviewModelForm
from .models import Review
from django.views import View

# Create your views here.
class ReviewsView(View):
    def get(self,request):
        form=ReviewModelForm()
        reviews=Review.objects.all()
        return render (request,"reviews.html",{"form":form,"reviews":reviews})
    def post(self,request):
        form=ReviewModelForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get("name")
            email=data.get("email")
            review=data.get("review")
            rate=data.get("rate")
            Review.objects.create(name=name,email=email,Review=review,rate=rate)
            return redirect("reviews")




def reviews(request):
    if request.method=="POST":
        form=ReviewModelForm(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get("name")
            email=data.get("email")
            review=data.get("review")
            rate=data.get("rate")
            Review.objects.create(name=name,email=email,Review=review,rate=rate)
            return redirect("reviews")
        
    form=ReviewModelForm()
    reviews=Review.objects.all()
    # with open("review.csv",mode="r",encoding="UTF-8") as file: 
    #     line=file.readline().split("|")
    #     if len(line)>0:
    #         name=line[0].capitalize()
    #         email=line[1]
    #         review=line[2]
    #         rate=line[3]
    #         print(line)
    #     else:
    #         name=" " 
    #         email=" "
    #         review=" "
    #         rate=" "

     # name=request.GET.get("name")
     # email=request.GET.get("email")
    # review=request.GET.get("review")
    return render (request,"reviews.html",{"form":form,"reviews":reviews})