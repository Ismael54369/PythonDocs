from django.shortcuts import render
from django.http import HttpResponse #Necesario para poder responder al cliente
from HolaMundo.models import Author
from HolaMundo.models import Book
from HolaMundo.forms import AuthorForm

# Create your views here.
#forma de responder al cliente cuando hace un http
def hola_mundo (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")
#Con esto hemos habilitado una vista, pero hay que además enlazar el proyecto con la
#aplicación

def home (request): # Pinta una página con render, también hay que darlo de alta en urls.py
    return render(request, "index.html")

def author (request): 
    author = Author.objects.all() #Devolver todos los registros de la tabla Author
    return render(request, "author.html", {'authors':author})

def book (request): 
    book = Book.objects.all()
    return render(request, "book.html", {'books':book})

def author_create (request):
    return render(request, 'author.html', {'author_form': AuthorForm}) #Si tenemos las páginas dentro de alguna
# carpeta dentro de template, entonces habría que especificar el nombre de la carpeta Ej:
# return render(request, 'nombre_carpeta/create_autor.html')



