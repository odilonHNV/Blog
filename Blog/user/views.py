from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect('blogApp:accueil')
        else:
            messages.info(request,"Identifiant ou mot de passe incorrect")
    form = AuthenticationForm()
    return render(request,'login_user.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('blogApp:accueil')
    

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('user:login-user')
    else:
        form = UserCreationForm()
    return render(request,'register_user.html',{'form':form})
    
