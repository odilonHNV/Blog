from django.db import models
from django.utils.text import slugify

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
    image = models.ImageField(upload_to='Image')

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title
    
