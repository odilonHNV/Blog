from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from user.models import UserProfil

class Etiquette(models.Model):
    name = models.CharField(max_length=20, unique=True,verbose_name='Nom')

    def __str__(self):
        return self.name


class Article(models.Model):
    
    class Categorie(models.TextChoices):
        Film = 'Film','Film'
        Jeux_vidéo = 'Jeux-vidéo','Jeux-vidéo'
        Livre = 'Livre','Livre'

    title = models.CharField(max_length=50, verbose_name='Titre Article')
    slug = models.SlugField(max_length=200,blank=True,verbose_name='Slug')
    description = models.TextField(max_length=1500,verbose_name='Description article')
    categorie = models.CharField(max_length=30, choices=Categorie.choices,verbose_name='Catégorie article')
    etiquette = models.ManyToManyField(Etiquette,blank=True,verbose_name='Etiquette(s) article')
    image = models.ImageField(upload_to='image/')

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
class Commentaire(models.Model):
    message_com = models.CharField(max_length=200) 
    #ForeignKey créé une relation de many to one entre le model(one) et un autre model(many)
    #ForeignKey créé une relation de many to one, un UserProfil peut etre associé à plusieurs commentaire
    user_com = models.ForeignKey(UserProfil, on_delete=models.CASCADE,verbose_name="Auteur")
    #C'est 'related_name' qui permet au model article d'accéder à commentaire
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Article",related_name="commentaire")
    date_dreation = models.DateTimeField(default=timezone.now,verbose_name="Date de création")

    
