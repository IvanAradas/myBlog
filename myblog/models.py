from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.OneToOneField(User)

	def __str__(self):
		return self.name.get_username()

class Post(models.Model):
	title = models.CharField('Titulo', max_length=32)
	content = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Author)

	def __str__(self):
		return self.title

class Comment(models.Model):
	author= models.CharField('Author', max_length=32)
	contenido = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.contenido
