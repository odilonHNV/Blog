from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import UserProfil

class UserProfilCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('email','username','password1','password2')

class ChangeProfilImageForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = ('user_image',)
        widgets = {
            'user_image':forms.FileInput(attrs={'class': 'form-control'})
        }
        """ Widgets: est un dictionnaire spécial dans les formulaires Django qui permet de 
            personnaliser l'affichage et le comportement des champs de formulaire.
            
            forms.FileInput() : est un widget spécifique pour les champs de téléchargement 
            de fichiers. Il crée un champ de type "file" dans le HTML.
            
            attrs={'class': 'form-control'} permet d'ajouter des attributs HTML au champ.

            attrs signifie "attributes" (attributs)
            'class': 'form-control' ajoute une classe CSS au champ de formulaire
            Dans ce cas, 'form-control' est une classe de Bootstrap qui donne un style standard aux champs de formulaire
            
        """

        #Le widget FileInput avec attrs={'class': 'form-control'} applique la classe CSS form-control à l'élément <input>.