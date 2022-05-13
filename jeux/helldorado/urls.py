from django.urls import path
from . import views
urlpatterns = [
    path("ajoutjoueur/",views.ajoutjoueur),
    path("traitementjoueur/",views.traitementjoueur),
    path("",views.index),
    path("joueurs/",views.listejoueur),
    path("<str:type>/delete/<int:id>/", views.delete),
    path("<str:type>/affiche/<int:id>/",views.affiche),
    path("<str:type>/update/<int:id>/",views.update),
    path("<str:type>/traitementupdate/<int:id>/",views.updatetraitement),
    path("<str:type>/ajout/<int:id>/",views.ajout),
    path("<str:type>/traitement/<int:id>/",views.traitement),
    path("faction/",views.faction),
    path("figurine/",views.figurine),
    path("keywords/",views.keywords),
    path("teams/",views.teams)
  #  path("<int:id>/ajoutfigurine/",views.ajoutfigurine)
]