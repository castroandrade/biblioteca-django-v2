from django.contrib import admin

from .models import Livro, Autor, Categoria

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Categoria)
