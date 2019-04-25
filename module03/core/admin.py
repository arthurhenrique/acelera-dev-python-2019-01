from django.contrib import admin

# Register your models here.
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created', 'updated', 'active')

admin.site.register(Autor, AutorAdmin)


