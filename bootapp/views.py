from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

    # Create your views here.
def login(request):
    return render(request,'login.html')

def baseHtml(request):
    return render(request, 'base.html')    

def home(request):
    return render(request, 'homes.html')

def aboutus(request):
    return render(request, 'aboutus.html')

