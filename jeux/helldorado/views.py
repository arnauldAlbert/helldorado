from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms

# Create your views here.
def ajoutjoueur(request):
    jform = forms.JoueurForm()
    return render(request,"helldorado/ajoutjoueur.html",{"jform" : jform})

def index(request):
    return render(request,"helldorado/index.html")

def traitementjoueur(request):
        jform = forms.JoueurForm(request.POST)
        if jform.is_valid:
            joueur = jform.save()
            return HttpResponseRedirect("/helldorado/joueurs/")
        else:
            return render(request,"helldorado/ajoutjoueur.html",{"jform" : jform})


def listejoueur(request):
    liste = list(models.Joueur.objects.all())
    return render(request,"helldorado/listejoueurs.html",{"liste" : liste})

def delete(request, type, id):
    if type == "joueur":
        joueur = models.Joueur.objects.get(pk = id)
        joueur.delete()
        return HttpResponseRedirect("/helldorado/joueurs/")
    elif type == "faction":
        faction = models.Faction.objects.get(pk=id)
        faction.delete()
        return HttpResponseRedirect(f"/helldorado/{type}/")
    elif type == "figurine":
        figurine = models.Figurine.objects.get(pk=id)
        figurine.delete()
        return HttpResponseRedirect(f"/helldorado/{type}/")
    else :
        return HttpResponseRedirect("/helldorado/joueurs/")

def affiche(request, type, id):
    if type == "joueur":
        joueur = models.Joueur.objects.get(pk=id)
        return render(request,"helldorado/affiche.html",{"type":type,"object": joueur})
    elif type == "faction" :
        faction = models.Faction.objects.get(pk=id)
        fig = list(models.Figurine.objects.filter(faction_id=id))
        return render(request, "helldorado/affiche.html", {"type": type, "object": faction, "liste":fig})
    elif type == "figurine":
        figurine = models.Figurine.objects.get(pk=id)
        keywords= figurine.keywords.all()
        return render(request, "helldorado/affiche.html", {"type": type, "object": figurine, "liste": keywords})
    elif type == "teams":
        teams = models.teams.objects.get(pk=id)
        figurine = teams.figurine.all()
        return render(request, "helldorado/affiche.html", {"type": type, "object": teams, "liste": figurine})
    else:
        return HttpResponseRedirect("/helldorado/joueurs/")


def update(request, type, id):
    if type == "joueur":
        joueur = models.Joueur.objects.get(pk=id)
        form = forms.JoueurForm(joueur.dico())
        return render(request,"helldorado/update.html",{"form":form,"id":id, "type":type})
    elif type == "faction":
        faction = models.Faction.objects.get(pk=id)
        form = forms.FactionForm(faction.dico())
        return render(request, "helldorado/update.html", {"form": form, "id": id, "type":type})
    elif type == "keywords":
        keywords = models.Keywords.objects.get(pk=id)
        form = forms.KeywordsForm(keywords.dico())
        return render(request, "helldorado/update.html", {"form": form, "id": id, "type": type})
    elif type == "figurine":
        figurine = models.Figurine.objects.get(pk=id)
        form = forms.FigurineForm(figurine.dico())
        return render(request, "helldorado/update.html", {"form": form, "id": id, "type": type})
    else :
        return HttpResponseRedirect("/helldorado/")

def updatetraitement(request, type, id):
    if type == "joueur":
        form = forms.JoueurForm(request.POST)
    elif type == "faction":
        form = forms.FactionForm(request.POST)
    elif type == "keywords":
        form = forms.KeywordsForm(request.POST)
    elif type == "figurine":
        form = forms.FigurineForm(request.POST)

    if form.is_valid():
         object = form.save(commit = False)
         object.id = id
         object.save()
         return HttpResponseRedirect(f"/helldorado/{type}/")
    else:
        return render(request,"helldorado/update.html",{"form":form,"id":id, "type":type})

def faction(request):
    liste = list(models.Faction.objects.all())
    return render(request, "helldorado/listefaction.html", {"liste": liste})

def ajout(request,type, id):
    if type == "faction":
        form = forms.FactionForm()
    elif type == "figurine":
        form = forms.FigurineForm()
    elif type == "keywords" :
        form = forms.KeywordsForm()
    elif type == "teams":
        form = forms.TeamsForm()
    return render(request, "helldorado/ajout.html", {"form": form, "type" : type, "id": id})

def traitement(request, type, id):
    if type == "faction":
        form = forms.FactionForm(request.POST)
    elif type == "figurine":
        form = forms.FigurineForm(request.POST)
    elif type == "keywords":
        form = forms.KeywordsForm(request.POST)
    elif type == "teams":
        form = forms.TeamsForm(request.POST)

    if form.is_valid():
        object = form.save(commit=False)
        if type == "faction" or type == "keywords" or type =="teams":
            object.save()
            return HttpResponseRedirect(f"/helldorado/{type}")
        elif type == "figurine":
            faction = models.Faction.objects.get(pk=id)
            object.faction_id = id
            object.faction = faction
            object.save()
            return HttpResponseRedirect(f"/helldorado/faction/affiche/{id}/")


    else:
        return render(request, "helldorado/ajout.html", {"form": form, "type": type, "id" : id})

def figurine(request):
    liste = list(models.Figurine.objects.all())
    return render(request, "helldorado/listefigurine.html", {"liste": liste})

def keywords(request):
    liste = list(models.Keywords.objects.all())
    return render(request, "helldorado/listekeywords.html", {"liste": liste})

def teams(request):
    liste = list(models.Teams.objects.all())
    return render(request,"helldorado/listeteams.html",{"liste": liste})

