from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuarios, Postagens
from .serializers import UsuariosSerializer, PostagensSerializer

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagens.objects.all()
    serializer_class = PostagensSerializer