from django.shortcuts import render
from . import models, forms

# Create your views here.
def ajoutjoueur(request):
    jform = forms.JoueurForm()
    return render(request,"helldorado/ajoutjoueur.html",{"jform" : jform})
