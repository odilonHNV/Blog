from django.contrib import admin
from blogApp.models import Article
from django.contrib import admin
from .models import Commentaire

# Username:Odilon  Pass:Odilon
admin.site.register(Article)

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('user','article','message_com','date_reaction') #Affiche ces champs dans la liste de l'admin 
    list_filter = ('user','article',)
    search_fields = ('message_com','user','article',) # Pour la recherche par commentaire,user et article 
