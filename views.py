from django import http
from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse



def curso(self):
    curso= Curso(nombre="Django", comision=93)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)
    
def inicio(request):
    return render (request, "Appcoder/inicio.html")
def cursos(self):
    return render (request, "Appcoder/cursos.html")
def profesores(self):
    return render (request, "Appcoder/profesores.html")
def estudiantes(self):
    return render (request, "Appcoder/estudiantes.html")
def entregables(self):
    return render (request, "Appcoder/entregables.html")               
