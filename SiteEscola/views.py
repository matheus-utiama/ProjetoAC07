from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render (request, "index.html")
	
def Noticias(request):
	return render (request, "Noticias.html")
	
def Disciplina(request):
	return render (request, "Disciplina.html")
	
def Lista_De_Cursos(request):
	return render (request, "Lista_De_Cursos.html")
	
def Detalhe_Curso(request):
	return render (request, "Detalhe Curso.html")
	
def Cadastro(request):
	return render (request, "Cadastro.html")
	
def Login(request):
	return render (request, "Login.html")