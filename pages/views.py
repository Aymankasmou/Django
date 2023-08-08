from django.shortcuts import render
from .models import login


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    user = request.POST.get('username')
    print(user)
    pas = request.POST.get('password')
    print(pas)
    data = login(username=user,password=pas)
    # data.save()
    return render(request, 'pages/about.html')
