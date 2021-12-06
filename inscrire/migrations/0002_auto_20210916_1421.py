# Generated by Django 3.1.7 on 2021-09-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscrire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filiere',
            name='RespoFiliere',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='filiere',
            field=models.ManyToManyField(through='inscrire.EnsFiliere', to='inscrire.Filiere'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='respoScolarite',
            field=models.ManyToManyField(through='inscrire.Inscription', to='inscrire.RespoScolarite'),
        ),
    ]
