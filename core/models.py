from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    dataEvento = models.DateTimeField(verbose_name='Data do evento')
    dataCriacao = models.DateTimeField(auto_now=True, verbose_name='Data da criação')#verbose = serve para mostrar como a variavel vai aparecer no site
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)#cascade = se o usuario for ixcluido, exclui tambem todos os eventos dele

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo


    def get_dataEvento(self):
        return self.dataEvento.strftime('%d/%m/%Y %H:%M H')

    def get_data_input_evento(self):
        return self.dataEvento.strftime('%Y-%m-%dT%H:%M')

