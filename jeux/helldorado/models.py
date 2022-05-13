from django.db import models
from django.utils import timezone
from datetime import date as dt
# Create your models here.

class Faction(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Faction des {self.nom} : \n {self.description}"

    def dico(self):
        return {"nom": self.nom, "description" : self.description}

class Keywords(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Mot clé {self.nom} : \n {self.description}"

    def dico(self):
        return {"name" : self.nom, "description" : self.description}

class Figurine(models.Model):
    GRADE = [
        ("officier", "Officier" ),
        ("independant", "indépendant"),
        ("troupier","troupier")
    ]
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length= 30, choices = GRADE, default="troupier")
    hit = models.IntegerField(blank=True)
    move = models.IntegerField()
    fight = models.IntegerField()
    defense = models.IntegerField()
    health = models.IntegerField()
    frequence = models.IntegerField(default=1)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keywords, blank=True)
    image = models.ImageField(default=None, upload_to="images", height_field=None, width_field=None)

    def add_keyword(self,kw):
        self.entry_set.add(kw)

    def dico(self):
        d = {"name": self.name, "grade": self.grade, "hit": self.hit, "move" : self.move,"fight": self.fight , "defense" : self.defense, "health" : self.health,"frequence" : self.frequence, "faction" : self.faction,"keywords" : self.keywords}

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    date_inscription = models.DateField(default= timezone.now)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'Joueur {self.nom}'

    def dico(self):
        return {"nom": self.nom, "date_inscription": self.date_inscription, "email": self.email}

class Teams(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(width_field=400, height_field=400, default=None)
    faction = models.ForeignKey(Faction,on_delete=models.CASCADE)
    liste = models.ManyToManyField(Figurine,through='TeamsList', symmetrical=False)

    def dico(self):
        return {"nom" : self.nom, "faction" : self.faction, "logo": self.logo, "liste" : self.liste}

class TeamsList(models.Model):
    team = models.ForeignKey("Teams",on_delete=models.CASCADE)
    figurine = models.ForeignKey("Figurine",on_delete=models.CASCADE)
    repetition = models.IntegerField(default=1, blank=True)




