from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


#why this because otherwise you can access homepage without login 
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('Password is not same')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('username or password is incorrect')
    return render(request,'login.html')

def LogOut(request):
    logout(request)
    return redirect('login')