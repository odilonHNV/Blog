from django.shortcuts import render,redirect,get_object_or_404
from blogApp.models import Article,Etiquette
from blogApp.forms import ArticleForm,CommentaireForm
from django.contrib import messages


def list_articles(request):
    articles = Article.objects.all()
    return render(request,'blogApp/list_articles.html',context={'articles':articles})

def detail_article(request,id):  
    article = get_object_or_404(Article,id=id)

    if request.method == 'POST':
        commentaire_form = CommentaireForm(request.POST)
        if commentaire_form.is_valid():
            #sauvergarde sans pour autant valider vers la base de donné
            commentaire=commentaire_form.save(commit = False)            
            commentaire.article=article
            commentaire.user_com = request.user.user_profil
            commentaire.save()     
            messages.success(request,"Commentaire bien créer")
            return redirect('blogApp:detail-article', id=article.id)
        else:
            messages.error(request,"Commentaire non créer, une erreur est survenue")
    else:
        commentaire_form = CommentaireForm()        
    
    context = { 'article':article,
                'commentaire_form':commentaire_form ,
                #Dans le model 'related_name' est important 
                'commentaires': article.commentaire.all()
            }
    return render(request,'blogApp/detail_article.html',context)

def create_article(request):    
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('accueil')
    else:
        article_form = ArticleForm()
    return render(request,'blogApp/create_article.html',context={'form':article_form})

def edit_article(request,id):
    article = Article.objects.get(id = id)    
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('accueil')
    else:
        article_form = ArticleForm(instance=article)
    return render(request,'blogApp/edit_article.html',context={'form':article_form})

def list_articles_same_etiquette(request,etiquette):
    etiquette_object = Etiquette.objects.get(name=etiquette)
    articles = Article.objects.filter(etiquette=etiquette_object)
    return render(request,'blogApp/list_articles_same_etiquette.html',context={'articles':articles})

def list_articles_same_categorie(request,categorie):
    articles = Article.objects.filter(categorie__iexact = categorie)
    print(articles)
    return render(request,'blogApp/list_articles_same_categorie.html',context={'articles':articles})