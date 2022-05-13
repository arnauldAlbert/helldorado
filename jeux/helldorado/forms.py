from django.forms import ModelForm
from django import forms
from . import models
from django.utils.translation import gettext_lazy as _
from datetime import date as dt

class FactionForm(ModelForm):
    class Meta:
        model = models.Faction
        fields = ("nom", "description")
        labels = {
            "nom": _("Nom de la faction"),
            "description" : _("Description de la faction")
        }

class FigurineForm(ModelForm):
    class Meta:
        model = models.Figurine
        fields = ("name" , "grade", "hit" , "move" ,
                  "fight" , "defense" , "health", "frequence","keywords","image")
        labels = {
            "name" : _(" Nom "),
            "hit" : _("Tir "),
            "move" : _("Déplacement"),
            "frequence" : _("frequence de la figurine dans une team "),
            "keywords" : _("Mots clés"),
            "image": _("photo de votre figurine"),
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nom","date_inscription","email")
        labels = {
            "nom": _("Nom "),
           "date_inscription": _("Date d'inscription"),
           "email": _("Adresse mail")
        }
        localized_fields = ("date_inscription",)
        widgets = {
           "date_inscription": forms.TextInput(attrs={'type': 'date', 'value': dt.today()}),
            "email": forms.EmailInput(attrs={'placeholder': 'prenom.nom@uha.fr'})
        }

class KeywordsForm(ModelForm):
    class Meta:
        model = models.Keywords
        fields = ("nom", "description")
        labels = {
            "nom": _("mot clé"),
        }

class TeamsForm(ModelForm):
    class Meta:
        model = models.Teams
        fields = ("nom", "logo", "faction")

