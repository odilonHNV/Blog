from blogApp import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',views.list_articles,name='accueil'),
    path('article/<int:id>/',views.detail_article,name='detail-article'),
    path('article/create/',views.create_article,name='create-article'),
    path('article/<int:id>/edit/',views.edit_article,name='edit-article'),
    #path('article/<int:id>/delete/',views.delete_article,name='delete-article')
    path('article/art/<str:etiquette>/',views.list_articles_same_etiquette,name='list-articles-same-etiquette'),
    path('article/<str:categorie>/',views.list_articles_same_categorie,name='categorie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
            document_root = settings.MEDIA_ROOT)