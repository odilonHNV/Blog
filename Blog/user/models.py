from django.db import models
from django.contrib.auth.models import User

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Utilisateur")
    user_image = models.ImageField(upload_to='Image/',blank=True,null=True)

    def __str__(self):
        return self.user.username