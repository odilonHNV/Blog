from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

app_name = "user" # Pour que la partie de mot de passe oublié fonctionne. Enlever cette ligne et revoir les autres liens.

urlpatterns = [
    path('login/',views.login_user,name='login-user'),
    path('logout/',views.logout_user,name='logout-user'),
    path('register/',views.register_user,name='register-user'),
    path('password_reset_user/',views.password_reset_user,name='password-reset-user'),
    path('change_profil_image/',views.change_profil_image,name='change-profil-image'),

    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name='password_reset'),
    
    path('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),
    
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'), 
]
"""
     J'ai pas implémenter la partie de mot de passe oublier
"""