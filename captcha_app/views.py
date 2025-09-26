from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def signed_in(request):
    return render(request, 'signed_in.html')
