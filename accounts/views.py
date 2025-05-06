from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:        
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                messages.info(request, 'user created')
                return redirect('login')
        
        else:
            messages.info(request, 'Password is not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')
    
def login(request):
      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = auth.authenticate(username=username, password=password)

          if user is not None:
              auth.login(request, user)
              return redirect('/')
          else:
              messages.info(request, 'invalid credentials')
              return redirect('login')
      else:
          return render(request, 'login.html') 
      

def logout(request):
    auth.logout(request)
    return redirect('/')

