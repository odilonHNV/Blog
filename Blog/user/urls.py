from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('login',views.login_user,name='login-user'),
    path('logout',views.logout_user,name='logout-user'),
    path('register',views.register_user,name='register-user'),
]
