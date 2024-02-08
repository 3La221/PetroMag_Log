from django.db import models

# Create your models here.

class Employee(models.Model):
    
    FAM_STATUS = (
        ('M','Marié'),
        ('C','Célibataire')
    )
    
    matricule = models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    date_recrut = models.DateField()
    date_detach = models.DateField()
    affect_origine = models.DateField()
    sit_fam = models.CharField(max_length=1, choices=FAM_STATUS)
    nbr_enfant = models.IntegerField(null = True , blank = True )
    
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} "
    
    
