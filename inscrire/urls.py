from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),

    #etudiant
    path("ajoutEtu", views.addEtu,name="ajoutEtu"),
    path("updateEtu/<str:pk>", views.updateEtu,name="updateEtu"),
    path("form", views.form_ins_etu,name="form"),
    path("saisiNote", views.saisiNote,name="saisiNote"),
    path("present", views.presence,name="present"),

    #Enseignant
    path("acceuilEns", views.acceuilEns,name="acceuilEns"),
    path("formEns", views.form_ins_ens,name="formEns"),
    path("ajoutEns", views.AddEns,name="ajoutEns"),
    path("desc", views.ajoutDesc,name="desc"),
    path("pres", views.ajoutPres,name="pres"),
    path("listeEns", views.listeEns,name="listeEns"),
    path("updateEns/<str:pk>", views.updateEns,name="updateEns"),

    #responsable de filiere
    path("acceuilFil", views.acceuilRespoFil,name="acceuilFil"),
    path("formFil", views.acceuilFormFiliere,name="formFil"),
    path("ajoutFil", views.AddFiliere,name="ajoutFil"),
    #path("updateFil/<str:pk>", views.updateFil,name="updateFil"),
    path("listeFil", views.listeFil,name="listeFil"),
    
    #Responsable de Scolarite
    path("acceuilRes", views.form_ins_etu,name="acceuilRes"),

    path("formReins", views.form_reins,name="formReins"),
    path("listeClasse", views.listeClasse,name="listeClasse"),
] 