from django.contrib import admin
from core.models import Evento


# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'dataEvento', 'dataCriacao')
    list_filter = ('usuario',)

admin.site.register(Evento, EventoAdmin)