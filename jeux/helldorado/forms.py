from django.forms import ModelForm
from django import forms
from . import models
from django.utils.translation import gettext_lazy as _
from datetime import date as dt

class FactionForm(ModelForm):
    nom = forms.CharField(label='Nom ', max_length= 30)
    description = forms.Textarea(label = "Description de la faction")

class FigurineForm(ModelForm):
    class Meta:
        model = models.Figurine
        fields = ("name" , "grade", "hit" , "move" ,
                  "fight" , "defense" , "health", "frequence" )
        labels = {
            "name" : _(" Nom "),
            "hit" : _("Tir "),
            "move" : _("Déplacement"),
            "frequence" : _("frequence de la figurine dans une team ")
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nom", "date_inscription", "email")
        labels = {
            "nom" : _("Nom "),
            "date_inscription" : _("Date d'inscription"),
            "email" : _("Adresse mail")
        }
        localized_fields = ("date_inscription")

        fields["date_inscription"].widget.attrs.update({'type': 'date', 'value': dt.today()})
        fields["email"].widget.attrs.update({'placeholder': 'prenom.nom@uha.fr'})