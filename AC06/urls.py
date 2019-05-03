from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns=[
	url(r'^admin/',admin.site.urls),
	url(r'^$', TemplateView.as_view(template_name='index.html')),
	url('Noticias',TemplateView.as_view(template_name='Noticias.html')),
	url('Cadastro',TemplateView.as_view(template_name='Cadastro.html')),
	url('Detalhe Curso',TemplateView.as_view(template_name='Detalhe Curso.html')),
	url('Disciplina',TemplateView.as_view(template_name='Disciplina.html')),
	url('Lista_De_Cursos',TemplateView.as_view(template_name='Lista_De_Cursos.html')),
	url('Login',TemplateView.as_view(template_name='Login.html')),
	url('index',TemplateView.as_view(template_name='index.html')),
	]