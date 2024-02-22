from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", {'produtos': produtos})
