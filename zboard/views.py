from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def login_user(request):
    if request.method == "POST":
        if request.POST["password"] != "purple":
            message = "Incorrect password"
            return render(request, "zboard/login.html", {"message": message})
        else:
            return redirect("home")

    return render(request, "zboard/login.html")


def home(request):
    return render(request, "zboard/home.html")
