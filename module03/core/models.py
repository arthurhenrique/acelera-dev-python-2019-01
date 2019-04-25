from django.db import models

class Base(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Updated em', auto_now=True)
    active = models.BooleanField('Ativo? ', default=True)


    class Meta:
        abstract = True


class Autor(Base):
    nome = models.CharField('Nome: ', max_length=100)
    email = models.EmailField('Email: ', max_length=100)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome

class Genero(Base):
    genero = models.CharField('Genero:', max_length=100)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.genero

class Livro(Base):
    titulo = models.CharField('Titulo:', max_length=100)
    genero = models.ForeignKey('core.Genero', verbose_name='Genero', on_delete=models.DO_NOTHING)
    autor = models.ManyToManyField('core.Autor', verbose_name='Autor')
    isbn = models.CharField ('ISBN', max_length=100)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo
