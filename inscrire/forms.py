from django import forms
from inscrire.models import Filiere, Enseignant, Etudiant

#formulaire de création de Filiere
class FiliereForm(forms.ModelForm):
	class Meta:
		model = Filiere
		fields = ["nomFiliere"]
		widgets={
			'nomFiliere':forms.TextInput(attrs={'class':'form-control'})
		}

	def clean_nomFiliere(self):
		nomFiliere = self.cleaned_data['nomFiliere']
		filieres =Filiere.objects.all()
		if nomFiliere in filieres:
			raise
			forms.ValidationError("cette filiere existe déjà !")
		return nomFiliere

#Formulaire d'ajout d'enseignant
class EnseignantForm(forms.ModelForm):
	class Meta:
		model = Enseignant
		fields = ["nom",'prenom','adresse', 'numTel','email','dateEntree','role','filiere']
		widgets={
			'nom':forms.TextInput(attrs={'class':'form-control'}),
			'prenom': forms.TextInput(attrs={'class':'form-control'}),
			'adresse': forms.TextInput(attrs={'class':'form-control'}),
			'numTel': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'dateEntree': forms.DateInput(attrs={'class':'form-control'}),
			'role': forms.TextInput(attrs={'class':'form-control'}),
			'filiere': forms.SelectMultiple(attrs={'class':'form-control'}),
			'password': forms.DateInput(attrs={'class':'form-control'}),
		}

#Formulaire d'ajout  d'étudiant
class EtudiantForm(forms.ModelForm):
	class Meta:
		model = Etudiant
		fields = ["nom",'prenom','adresse', 'numTel','email','dateEntree','delegue','dateNaiss','lieuNaiss','password']
		widgets={
			'codePermanent':forms.NumberInput(attrs={'class':'form-control'}),
			'nom':forms.TextInput(attrs={'class':'form-control'}),
			'prenom': forms.TextInput(attrs={'class':'form-control'}),
			'adresse': forms.TextInput(attrs={'class':'form-control'}),
			'numTel': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'dateNaiss': forms.DateInput(attrs={'class':'form-control'}),
			'lieuNaiss': forms.TextInput(attrs={'class':'form-control'}),
			'dateEntree': forms.DateInput(attrs={'class':'form-control'}),
			'delegue': forms.CheckboxInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
		}