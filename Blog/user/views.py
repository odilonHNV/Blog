from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.forms import UserProfilCreationForm
from django.contrib import messages
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username = username, password = password)
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
        form = UserProfilCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('user:login-user')
    else:
        form = UserProfilCreationForm()
    return render(request,'register_user.html',{'form':form})
    
def password_reset_user(request):
    if request.method=='POST':
        username = request.user.username
        password_current = request.POST["password_current"]
        user_pass = authenticate(request,username=username,password = password_current)
        if user_pass is not None:
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            if password1==password2:
                user_current = User.objects.get(id = request.user.id)

                user_current.set_password(password1) #Cette ligne permet de hashé le mot de pass
                user_current.save()
                update_session_auth_hash(request,user_current) #Cette ligne permet de maintenir l'utilisateur connecté

                messages.success(request,"Mot de passe modifier avec succès")
                return redirect('blogApp:accueil')
            else:
                messages.error(request,"les deux mot de passes enter ne se correspondent pas. Entrer deux mot de passes identique")
        else:
            messages.error(request,"Le mot de passe actuel est incorrect. Veillez entrer un mot de pass correct")
    return render(request,'password_reset_user.html')