from django import forms
from HolaMundo.models import Author # importamos el modelo que nos hace falta, en este caso necestimos insertar autores
#Creamos nuestro primer Form
class AuthorForm (forms.ModelForm): #Vamos a crear un formulario de Django , basado en un modelo, por eso hacemos la herencia
    class Meta:
        model=Author
        fields='__all__'