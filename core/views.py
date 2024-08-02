from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def sign_up(request):
    return render(request, "core/sign_up.html")