from django.shortcuts import render,redirect
from inscrire.models import Etudiant,Inscription,RespoScolarite,Filiere
from inscrire.forms import FiliereForm, EnseignantForm, EtudiantForm
from django.http import HttpResponse

#page d'acceuil
def home(request):
	return render(request,"auth.html")

#formulaire inscription étudiant
def form_ins_etu(request):
	form = EtudiantForm()
	return render(request,"RespoScolarite/form-ins-etu.html",{'form':form})

#formulaire de création de filière
def acceuilFormFiliere(request):
	form = FiliereForm()
	return render(request,"RespoFiliere/form_filiere.html",{'form':form})

#formulaire inscription enseignant
def form_ins_ens(request):
	form = EnseignantForm()
	return render(request,"RespoFiliere/form_ins_ens.html",{'form':form})


#formulaire de réinscription
def form_reins(request):
	return render(request,"form_reins1.html")

#Ajout Description
def ajoutDesc(request):
	return render(request,"Enseignant/description.html")

#Ajout Présentation
def ajoutPres(request):
	return render(request,"Enseignant/presentation.html")

#page d'acceuil du professeur
def acceuilEns(request):
	return render(request,"Enseignant/acceuil.html")

#page d'acceuil du professeur
def acceuilRespoFil(request):
	return render(request,"RespoFiliere/acceuil.html")

#Sairir note
def saisiNote(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"Enseignant/saisirNote.html",context)

#lister les étudiants
def listeClasse(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"RespoScolarite/form-list-etu.html", context)

#lister les enseignants
def listeEns(request):
	enseignants = Enseignant.objects.all()
	context ={
		'enseignants':enseignants
	}
	return render(request,"RespoFiliere/liste-ens.html", context)

#lister les filieres
def listeFil(request):
	filieres = Filiere.objects.all()
	context ={
		'filieres':filieres
	}
	return render(request,"RespoFiliere/list-fil.html", context)

#Formulaire d'incription des présence
def presence(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"Enseignant/listPresence.html", context)



def AddFiliere(request):
	form = FiliereForm(request.POST)
	if request.method == "POST":
		nomFil=request.POST.get("nomFiliere")
		filieres =Filiere.objects.all()
		if nomFil in filieres:
			return HttpResponse("Cette filiere a été déjà enregistré ")
			
		else:
			if form.is_valid():
				try:
					form.save()
				except:
					pass
	return render (request, 'RespoFiliere/acceuil.html',{'form':form})
	#return render (request, 'RespoFiliere/form_filiere.html',{'form':form})		
				

	#else:
		#form = FiliereForm()
	

#Ajouter un enseignant dans la base de données
def AddEns(request):
	if request.method == "POST":
		form = EnseignantForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("formEns")
			except:
				pass
	else:
		form = EnseignantForm()
	return render (request, 'RespoFiliere/form_ins_ens.html',{'form':form})

#modifier Enseignant
def updateEns(request, pk):
	ens = Enseignant.objects.get(id=pk)
	form =EnseignantForm(instance= ens)
	if request.method == "POST":
		form = EtudiantForm(request.POST, instance=ens)
		if form.is_valid():
			try:
				form.save()
				return redirect("formEns")
			except:
				pass
	else:
		form = EnseignantForm()
	return render (request, 'RespoFiliere/form_ins_ens.html',{'form':form})

	
#Ajouter un étudiant dans la base de données
def addEtu(request):
	if request.method == "POST":
		form = EntudiantForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect("formEtu")
			except:
				pass
	else:
		form = EtudiantForm()
	return render (request, 'RespoFiliere/form_ins_etu.html',{'form':form})


#modifier Etudiant
def updateEtu(request, pk):
	etu = Etudiant.objects.get(id=pk)
	form =EtudiantForm(instance= etu)
	if request.method == "POST":
		form = EtudiantForm(request.POST, instance=etu)
		if form.is_valid():
			try:
				form.save()
				return redirect("formEtu")
			except:
				pass
	return render (request, 'RespoScolarite/form-ins-etu.html',{'form':form})



