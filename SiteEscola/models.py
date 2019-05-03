from django.db import models

class Disciplina (models.Model):
	Nome_Curso = models.CharField("Nome_Curso", max_length=50)
	Nome_Disciplina = models.CharField("Nome_Disciplina", max_length=50)
	Semestre = models.CharField("Semestre", max_length=30)
	def _str_(self):
		return self.nome

class Usuarios (models.Model):
	login = models.CharField ("login", max_length=50)
	senha = models.CharField ("senha", max_length=50)
	Tipo_Usuario = models.IntegerField("Tipo_Usuario")
	def _str_(self):
		return self.nome
		
class Aluno (models.Model):
	RA = models.CharField ("RA", max_length=50)
	Nome_Aluno = models.CharField ("Nome_Aluno", max_length=50)
	Sobrenome = models.CharField ("Sobrenome", max_length=100)
	Genero = models.CharField ("Genero", max_length=1)
	Endereco = models.CharField ("Endereco", max_length=100)
	Telefone = models.CharField ("Telefone", max_length=11)
	Email = models.CharField ("Email", max_length=100)
	def _str_(self):
		return self.nome

class Professor (models.Model):
	RP = models.CharField ("RP", max_length=50)
	Nome_Professor = models.CharField ("Nome_Professor", max_length=50)
	Sobrenome = models.CharField ("Sobrenome", max_length=100)
	Genero = models.CharField ("Genero", max_length=1)
	Endereco = models.CharField ("Endereco", max_length=100)
	Telefone = models.CharField ("Telefone", max_length=11)
	Email = models.CharField ("Email", max_length=100)
	def _str_(self):
		return self.nome

