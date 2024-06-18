
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect
from .models import Proyecto, Contacto
from .forms import ContactoForm

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos': proyectos})

#vistas del crud administracion de usuarios 

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'myporfolio/contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request,'myporfolio/contacto_detalle.html', {'contacto': contacto})
 

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=Contacto)
    return render(request, 'myporfolio/contacto_formulario.html',{'form': form})
#contacto eliminar

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'myporfolio/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'myporfolio/contacto_confirmacion.html')
