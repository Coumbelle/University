from django.db import models
from django.forms import ModelForm,Textarea
from django.utils import timezone

# Create your models here.
class Filiere(models.Model):
	nomFiliere =models.CharField(max_length=60,unique=True, blank=False)

class Meta:
	db_table = "filiere"

class Enseignant(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse=models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	password = models.CharField(max_length=60, blank=False)
	dateEntree = models.DateTimeField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant")
	dateSortie = models.DateField(null=True)
	role =models.CharField(max_length=60)
	filiere = models.ManyToManyField(Filiere, through='EnsFiliere')
	
class RespoScolarite(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse =models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	password = models.CharField(max_length=60, blank=False)

class Etudiant(models.Model):
	codePermanent = models.IntegerField()
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse =models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	dateNaiss = models.DateField()
	lieuNaiss =models.CharField(max_length=60, blank=False)
	dateEntree = models.DateField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant")
	dateSortie = models.DateField(null=True)
	delegue =models.BooleanField(default=False)
	respoScolarite = models.ManyToManyField(RespoScolarite, through='Inscription')
	password = models.CharField(max_length=60, blank=False)

class Inscription(models.Model):
	anneeScolaire = models.CharField(max_length=60, blank=False)
	etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
	respoScolarite = models.ForeignKey(RespoScolarite, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

class Ec(models.Model):
	codeEc = models.CharField(max_length=60, blank=False)
	nomEc = models.CharField(max_length=60, blank=False)
	presentation = models.TextField(null=True)
	description = models.TextField(null=True)
	enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)



class EnsFiliere(models.Model):
	RespoFiliere = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)


class Modalite(models.Model):
	fraisInscription = models.IntegerField()
	mensualite = models.IntegerField()
	filiere = models.ManyToManyField(Filiere, through='ModFiliere')

class ModFiliere(models.Model):
	modalite = models.ForeignKey(Modalite, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

class Niveau(models.Model):
	nomNiveau = models.CharField(max_length=60)
	numNiveau = models.IntegerField()
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)