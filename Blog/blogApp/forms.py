from django import forms
from blogApp.models import Article,Commentaire

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
    
class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields =( 'message_com',)