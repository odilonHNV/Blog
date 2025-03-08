from django.shortcuts import render,redirect
from blogApp.models import Article,Etiquette
from blogApp.forms import ArticleForm


def list_articles(request):
    articles = Article.objects.all()
    return render(request,'blogApp/list_articles.html',context={'articles':articles})

def detail_article(request,id):
    article = Article.objects.get(id=id)
    return render(request,'blogApp/detail_article.html',context={'article':article})

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