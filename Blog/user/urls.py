from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path('login/',views.login_user,name='login-user'),
    path('logout/',views.logout_user,name='logout-user'),
    path('register/',views.register_user,name='register-user'),
    path('password_reset_user/',views.password_reset_user,name='password-reset-user'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]
