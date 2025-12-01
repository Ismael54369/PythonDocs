from django.shortcuts import render
from django.http import HttpResponse #Necesario para poder responder al cliente

# Create your views here.
#forma de responder al cliente cuando hace un http
def hola_mundo (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")
#Con esto hemos habilitado una vista, pero hay que además enlazar el proyecto con la
#aplicación

def home (request):
    return render(request, "index.html")

