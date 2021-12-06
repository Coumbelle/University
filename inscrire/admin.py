from django.contrib import admin
from .models import Enseignant
from .models import	Etudiant
from .models import	RespoScolarite
from .models import Ec
from .models import Inscription
from .models import Filiere
from .models import Niveau
from .models import Modalite

# Register your models here.
admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(RespoScolarite)
admin.site.register(Ec)
admin.site.register(Inscription)
admin.site.register(Filiere)
admin.site.register(Niveau)
admin.site.register(Modalite)