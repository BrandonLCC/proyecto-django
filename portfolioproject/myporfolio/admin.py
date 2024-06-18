from django.contrib import admin
from .models import Categoria, Tecnologias, Proyecto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tecnologias)
admin.site.register(Proyecto)