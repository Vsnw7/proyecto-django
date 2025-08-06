from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos, Archivos   #Accedemos la modelo alumno que contiene la estructura de la tabla
from .forms import ComentarioContactoForm, FormArchivos
from .models import ComentarioContacto
from django.contrib import messages
import datetime


from django.db.models import Q


#def registros (request):
    #alumnos=Alumnos.objects.all() #all recupera todos los objetos del modelo(registros de la tabla alumnos)
    #return render(request, "registros/principal.html",{'alumnos':alumnos})
    #Indicamos el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados


def registros(request):
    query = request.GET.get('q') 
    if query:
        alumnos = Alumnos.objects.filter(
            Q(nombre__icontains=query) | Q(matricula__icontains=query)
        )
    else:
        # Si el usuario no escribió nada, mostramos todos los alumnos
        alumnos = Alumnos.objects.all()

    # Renderizamos la plantilla y le enviamos la lista de alumnos y el texto de búsqueda para que pueda mostrarse en el campo de búsqueda
    return render(request, "registros/principal.html", {'alumnos': alumnos, 'query': query})



def registrar(request):
    if request.method == 'POST':
        form=ComentarioContactoForm(request.POST)
        if form.is_valid():  #si los datos recibidos son correctos
            form.save()  #inserta
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    form=ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulariolos datos ingresados
    return render(request, 'registros/contacto.html', {'form':form})


def contacto(request):
    return render(request, "registros/contacto.html")
    #Indicamos el lugar donde se realizara el resultado de esta vista


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})


def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario=get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objeto
    #del modelo que cumple la condición (registro de la tabla ComentariosContacto.)
    #get se emplea cuando se sabe que solo hay un onjeto que coincide con su consulta
    
    return render(request, "registros/formEditarComentario.html", {'comentario':comentario})
    #Indicamos el lugar donde se renderizará el resultado de esta vista y enviamos la lista de alumnos recuperados


def editarComentarioContacto(request, id):
    comentario=get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica
        comentarios=ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})
    #Si el formulario no es valido nos regresa al formulario para verificar datos
    return render(request, "registros/formEditarComentario.html", {'comentario':comentario})



def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render (request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo':Archivos})
    


























#La función FILTER nos retornará los registros que coinciden con los parámetros de busqueda datos 
def consultar1(request):
    #con una sola condición
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar2(request):
    #con una sola condición
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar3(request):
    #Si solo deseamos recuperar ciertos datos agregamos la funcion only
    #listando los campos que queremos obtener de la consulta, emplear
    #filter() o en el ejemplo all()
    alumnos=Alumnos.objects.all().only("matricula", "nombre", "carrera", "turno", "imagen")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar4(request):
    #con la expresion __contains
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar6(request):
    fechaInicio=datetime.date(2025, 7, 9)
    fechaFin=datetime.date(2025, 7, 23)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def consultar7(request):
    #Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains="No inscrito")
    return render (request, "registros/consultas.html", {'alumnos':alumnos})



def consultarComentario1(request):
    fechaInicio=datetime.date(2025, 7, 8)
    fechaFin=datetime.date(2025, 7, 9)
    comentarios=ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})


def consultarComentario2(request):
    #con la expresion __contains
    comentarios=ComentarioContacto.objects.filter(mensaje__contains="Comen")
    return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})


def consultarComentario3(request):
    comentarios=ComentarioContacto.objects.filter(usuario__in=["vanessa t"])
    return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})


def consultarComentario4(request):
    comentarios=ComentarioContacto.objects.filter().only("mensaje")
    return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})


def consultarComentario5(request):
    #con una sola condición
    comentarios=ComentarioContacto.objects.filter(usuario="luis editado")
    return render(request, "registros/consultaContacto.html", {'comentarios':comentarios})


def ConsultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'alumnos':alumnos})


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render (request, "registros/seguridad.html", {'nombre':nombre})
