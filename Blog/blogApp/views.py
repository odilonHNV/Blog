from django.shortcuts import render,redirect,get_object_or_404
from blogApp.models import Article,Etiquette
from blogApp.forms import ArticleForm,CommentaireForm
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.db.models import Q

# Username:Odilon  Pass:Odilon
"""
    Pour exemple de permission pour le user
        user.has_perm()
            .all()  les permissions à ajouter à l'utilisateur courant
            .add(<perm1>,<perm2>,...) ajout des permissions citer
            .remove(<perm1>,<perm2>,...) supprime des permissions citer
            .set([]) citer les permissions à ajouter à l'utilisateur courant
            .clear() Supprime toute les permission pour l'utilisateur courrant
"""


def list_articles(request):
    articles = Article.objects.all()
    if request.method == 'GET':
        word_search = request.GET.get('recherche')
        if word_search is not None:
            articles = Article.objects.filter( Q(title__icontains = word_search) |
                                               Q(description__icontains = word_search)
                                             )
    return render(request,'blogApp/list_articles.html',{'articles':articles})


def list_article_admin(request):
    articles = Article.objects.all()
    return render(request,'blogApp/list_article_admin.html',{'articles':articles})

def detail_article(request,id):  
    article = get_object_or_404(Article,id=id)
    if request.method == 'POST':
        commentaire_form = CommentaireForm(request.POST)
        if commentaire_form.is_valid():
            #sauvergarde sans pour autant valider vers la base de donné
            commentaire=commentaire_form.save(commit = False)            
            commentaire.article=article
            commentaire.user = request.user.user_profil
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
                'commentaires': article.commentaire.order_by('-date_reaction')
            }
    return render(request,'blogApp/detail_article.html',context)

@permission_required("blogApp.view_article",raise_exception = True)
def create_article(request):    
    if request.method == 'POST':
        article_form = ArticleForm(request.POST,request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('accueil')
    else:
        article_form = ArticleForm()
    return render(request,'blogApp/create_article.html',context={'form':article_form})

@permission_required("blogApp.change_article", login_url= "blogApp:error")
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

@permission_required("blogApp.delete_article", login_url="blogApp:error")
def delete_article(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method=='POST':
        article.delete()
        return redirect('blogApp:accueil')
    return render(request,'blogApp/delete_article.html')

def list_articles_same_etiquette(request,etiquette):
    etiquette_object = Etiquette.objects.get(name=etiquette)
    articles = Article.objects.filter(etiquette=etiquette_object)
    return render(request,'blogApp/list_articles_same_etiquette.html',context={'articles':articles})

def list_articles_same_categorie(request,categorie):
    articles = Article.objects.filter(categorie__iexact = categorie)
    return render(request,'blogApp/list_articles_same_categorie.html',context={'articles':articles})

def error(request):
    return render(request,'blogApp/error.html')