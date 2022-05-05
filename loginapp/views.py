from django.contrib import messages
from turtle import home
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout




# Create your views here.
def index(request):
    return render(request,'index.html')

# def home(request):
#     return render(request,'home.html')    

def user_login(request):
    if 'username' in request.session :
        return redirect(home)
    if request.method == 'POST' :
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(username=username, password=password)
         if user is not None :
             request.session['username'] = username
             return redirect(home)
         else :
             messages.error(request,'invalid username or password')
             print('invaid credentials')
    return render(request,'index.html')



def home(request):  
    if 'username' in request.session :

        return render(request, 'home.html')
    return redirect(user_login)    

def user_logout(request):
    if 'username' in request.session :
        request.session.flush()
    return redirect(user_login)                      