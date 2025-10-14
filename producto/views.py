from django.shortcuts import render, redirect,get_object_or_404
from .models import Productos
from .forms import ProductoForm
# Libreria para usar xhtml2pdf
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
# Create your views here.


# Crear el index
def lista_producto(request):
    producto = Productos.objects.all()
    context = {
        'producto': producto
    }
    return render(request, 'listado.html', context)

# Crear Producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_producto')
    else:
        form = ProductoForm()
    context = {'form': form}
    return render(request, 'crear_producto.html', context)

def editar_producto(request, id):
    productos = get_object_or_404(Productos, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=productos)
        if form.is_valid():
            form.save()
            return redirect('lista_producto')
    else:
        form = ProductoForm(instance=productos)
    context = {'form': form}
    return render(request, 'crear_producto.html', context)

def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_producto')
    return render(request, 'eliminar_producto.html', {'producto': producto})



def enviar_pdf_email(request):
    # 1️⃣ Cargar template HTML con datos
    template = get_template('pdf.html')
    context = {'producto': Productos.objects.all()}
    html = template.render(context)

    # 2️⃣ Crear PDF en memoria
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')

    pdf_buffer.seek(0)  # volver al inicio del buffer

    # 3️⃣ Crear correo
    email = EmailMessage(
        subject='📦 Reporte de productos',
        body='Adjunto encontrarás el reporte de productos en PDF.',
        from_email='andycontreras123456@gmail.com',
        to=['acaa83406@gmail.com'],  # <--- cambia aquí
    )

    # 4️⃣ Adjuntar PDF
    email.attach('reporte_productos.pdf', pdf_buffer.read(), 'application/pdf')

    # 5️⃣ Enviar correo
    email.send()

    return HttpResponse('<h2>Correo enviado correctamente con el PDF adjunto ✅</h2>')