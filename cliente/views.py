from django.shortcuts import render, HttpResponse
from .models import Cliente


# Create your views here.
def inicio(request):
    #return HttpResponse("this is the equivalent of @app.route('/'!")
    return render(request, "index.html")

def agregar(request):
    #request.post['parametro] -> Capturamos los parametros del formulario
    Cliente.objects.create(
        nombre = request.POST['nombre'],
        apellido = request.POST['apellido'],
        rut = request.POST['rut'],
        dv = request.POST['dv'],
        email = request.POST['email'],
        password = request.POST['password'],
        direccion = request.POST['direccion'],
    )
    return render(request, "index.html")

def leer(request):
    clientes = Cliente.objects.all()
    return render(request, "index.html")

def actualizar(request):
    id = request.POST['id'] #Tremos el ID de la variable
    cliente = Cliente.objects.get(id=id) #Con el ID traemos el registro como un objeto
    errores = Cliente.objects.validado(request.POST) # Se ejecuta el metodo