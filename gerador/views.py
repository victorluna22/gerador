from datetime import datetime
from django.shortcuts import render
from gerador.models import Imovel

# Create your views here.


def gera_texto(request, id):
	imovel = Imovel.objects.get(id=id)
	return render(request, 'gerador/texto.html', {'imovel': imovel, 'today': datetime.today().strftime('%d de %b %Y')})