from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

# Create your views here.
def home(request):
    return render(request,'Home/home.html')

def signup(request):
    if request.method=="POST":
      firstname=request.POST['firstname']  
      lastname=request.POST['lastname']  
      email=request.POST['email']  
      username=request.POST['username']  
      password=request.POST['password']  
      confirmpassword=request.POST['confirmpassword']  
      my_user=User.objects.create_user(username,email,password)
      my_user.first_name=firstname
      my_user.last_name=lastname
      my_user.save()
      
      messages.success(request,"YOUR ACCOUNT AS CRREATED SUCESSFULLY!!")
      return redirect('login')

    return render(request,'SignUp/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use the aliased auth_login function
            firstname=user.first_name
            return render(request, 'Home/home.html',{"firstname":firstname})
        else:
            messages.error(request, "Your username and password do not match")
            return redirect('home')

    return render(request, 'Login/login.html')

def signout(request):
    logout(request)
    return redirect('login')
