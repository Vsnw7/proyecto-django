
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_registros
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('contacto/',views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('registrar/',views_registros.registrar, name="Registrar" ),
    path('comentarios/', views_registros.consultarComentario, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('subir', views_registros.archivos, name='Subir'),






    path('consultar1', views_registros.consultar1, name='Consultas'),
    path('consultar2', views_registros.consultar2, name='Consultas'),
    path('consultar3', views_registros.consultar3, name='Consultas'),
    path('consultar4', views_registros.consultar4, name='Consultas'),
    path('consultar5', views_registros.consultar5, name='Consultas'),
    path('consultar6', views_registros.consultar6, name='Consultas'),
    path('consultar7', views_registros.consultar7, name='Consultas'),
    path('consultarComentario1', views_registros.consultarComentario1, name='Consultas'),
    path('consultarComentario2', views_registros.consultarComentario2, name='Consultas'),
    path('consultarComentario3', views_registros.consultarComentario3, name='Consultas'),
    path('consultarComentario4', views_registros.consultarComentario4, name='Consultas'),
    path('consultarComentario5', views_registros.consultarComentario5, name='Consultas'),
    path('ConsultasSQL', views_registros.ConsultasSQL, name='Consultas SQL'),
    path('seguridad', views_registros.seguridad, name='seguridad'),
]   

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)