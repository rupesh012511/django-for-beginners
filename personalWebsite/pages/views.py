from django.shortcuts import render

from django.http import HttpResponse

def home_page_view(Request):
    return HttpResponse("Home Page")

def about_page_view(Request):
    context = {"name":"Rupesh Rakesh Chaurasia",
               "age": 20
               }
    return render(Request,"pages/about.html", context)