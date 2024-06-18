from django.db import models
from .utils import encrypt_message, decrypt_message
# Create your models here.


#Modelo para categorias 
class Categoria(models.Model):
    nombre = models.CharField(max_length =100,unique=True)

#def es como una funcion
def __str__(self):
    return self.nombre

#Modelos tecnologias que estemos utilizando en el proyecto
class Tecnologias(models.Model):
    nombre = models.CharField(max_length =50,unique=True)

def __str__(self):
    return self.nombre

#Modelo proyectos del portafolio
class Proyecto (models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologias)
    link_sitio = models.URLField(max_length=200)
    link_repositorio = models.URLField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

def __str__(self):
    return self.titulo


#....
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    mensaje_cifrado = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

def save(self, *args, **kwargs):
    self.mensaje_cifrado = encrypt_message(self.mensaje)
    super().save(*args,**kwargs)

def get_mensaje(self):
    return decrypt_message(self.mensaje_cifrado)
    
def __str__(self):
    return self.nombre ##Devuelve el nombre del conctacto
