from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from .forms import RegisterForm


def index(request):
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


def registerView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username') # for filter out username from newly created user
            messages.success(request,'New Account Is created For' + user) # to display success message for user
            # this message will be displayed in login template
            return redirect('login')

    else:
        form=RegisterForm()
    return render(request, 'registration/register.html',{"form":form})