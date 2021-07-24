from django.shortcuts import render, redirect 
from django.contrib.auth.models import User,auth
from django.contrib import messages
#from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=user, password=pass1)
        if user == None:
            messages.info(request,"username or Password doesn't match")
            return redirect('signin')
        else:
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2 :
            messages.info(request,"password didn't match")
        if (User.objects.filter(username=username).exists()) and (User.objects.filter(email=email).exists()):
            messages.info(request,"username/email already taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(password=pass1,username=username,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect('/')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')