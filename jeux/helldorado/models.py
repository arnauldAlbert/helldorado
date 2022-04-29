from django.db import models


# Create your models here.

class Faction(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Faction des {self.nom} : \n {self.description}"

    def dico(self):
        return {"nom": self.nom, "description" : self.description}

class Keywords(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"Mot clé {self.nom} : \n {self.description}"

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
    keywords = models.ManyToManyField(Keywords, symmetrical=False)

    def add_keyword(self,kw):
        self.entry_set.add(kw)

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    date_inscription = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f'Joueur {self.nom}'

class Teams(models.Model):
    nom = models.CharField(max_length=100)
    faction = models.ForeignKey(Faction,on_delete=models.CASCADE)
    liste = models.ManyToManyField(Figurine,symmetrical=False)

