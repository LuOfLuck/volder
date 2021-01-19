from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "volder/main.html")

def trabajo(request):
    return render(request, "volder/trabajo.html")