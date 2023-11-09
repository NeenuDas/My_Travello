from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is  not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return  render(request,"login.html")

def form(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME Already Exist")
                return redirect('form')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('form')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                return  redirect('login')

                #print("USER CREATED SUCCESSFULLY")
        else:
            messages.info(request,"Password Not matched")
            return redirect('form')
            return redirect('/')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')