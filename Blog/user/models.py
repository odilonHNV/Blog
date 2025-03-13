from django.db import models
from django.contrib.auth.models import User
               

class UserProfil(models.Model):
    #'related_name' est important
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profil")
    user_image = models.ImageField(upload_to='Image/',blank=True,null=True)

    def __str__(self):
        return self.user.username
    

