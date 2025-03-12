from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogApp import views

app_name="blogApp"

urlpatterns = [
    path('',views.list_articles,name='accueil'),
    path('<int:id>/',views.detail_article,name='detail-article'),
    path('create/',views.create_article,name='create-article'),
    path('<int:id>/edit/',views.edit_article,name='edit-article'),
    #path('<int:id>/delete/',views.delete_article,name='delete-article'),
    path('etiquette/<str:etiquette>/',views.list_articles_same_etiquette,name='list-articles-same-etiquette'),
    path('categorie/<str:categorie>/',views.list_articles_same_categorie,name='categorie'),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL,
                document_root = settings.MEDIA_ROOT
    )