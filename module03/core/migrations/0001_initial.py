# Generated by Django 2.2 on 2019-04-25 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo? ')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome: ')),
                ('email', models.EmailField(max_length=100, verbose_name='Email: ')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo? ')),
                ('genero', models.CharField(max_length=100, verbose_name='Genero:')),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo? ')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo:')),
                ('isbn', models.CharField(max_length=100, verbose_name='ISBN')),
                ('autor', models.ManyToManyField(to='core.Autor', verbose_name='Autor')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Genero', verbose_name='Genero')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
