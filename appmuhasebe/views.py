from django.shortcuts import render, redirect

def index(request):
    return render(request, "appmuhasebe/index.html")

def defterolur(request):
    return render(request, "appmuhasebe/defterolur.html")
