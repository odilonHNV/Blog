from django.contrib import admin
from user.models import UserProfil


@admin.register(UserProfil)
class UserProfilAdmin(admin.ModelAdmin):
    list_display = ('user__username','user__email','user_image')
    search_fields =('user__username','user__email',) # Permet la recherche par nom d'utilisateur et par mail