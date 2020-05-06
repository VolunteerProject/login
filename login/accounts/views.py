from django.shortcuts import render,redirect
#from .models import Post
from .forms import RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages # to throw flash message for successful login or error
# Create your views here.


'''def indexView(request):
    return render(request,'index.html')'''


def index(request):
    '''context = {
        #'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }'''

    return render(request, 'index.html')


def userlogin(request):
    if request.method=='Post':
        username=request.Post.get('username')
        password=request.Post.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username or password is incorrect')

    return render(request, 'registration/login1.html')


def registerView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username') # for filter out username from newly created user
            messages.success(request,'New Account Is created For'+user) # to display success message for user
            # this message will be displayed in login template
            return redirect('login')

    else:
        form=RegisterForm()
    return render(request, 'registration/register.html',{"form":form})
