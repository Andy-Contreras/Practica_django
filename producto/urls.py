from django.urls import path
from . import views


urlpatterns = [
    path('',views.lista_producto, name='lista_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('enviar_pdf/', views.enviar_pdf_email, name='enviar_pdf_email'),

]