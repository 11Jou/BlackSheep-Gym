from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

def form(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('pass')
        accountData = Account(Name = name , Mail = mail , Password = password)
        if Account.objects.filter(Mail = mail).exists() == False:
            if (password2 == password):
                userData = User.objects.create_user(name, mail , password)
                accountData.save()
                userData.save()
                return redirect('login')
            else:
                return render(request, 'signup.html' , {'message':"Password Don't Match"})
        else:
            return render(request, 'signup.html', {'message2':"This email is already exist"})
    else : 
        return render(request , 'signup.html')


def signin(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'msg':"Username or Password is Wrong !"})
    else:
        return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('/')

