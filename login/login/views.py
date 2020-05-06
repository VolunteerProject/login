from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    '''context = {
        #'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }'''

    return render(request, 'index.html')

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username or password is incorrect')
            return render(request, 'registration/login1.html')

    return render(request, 'registration/login1.html')