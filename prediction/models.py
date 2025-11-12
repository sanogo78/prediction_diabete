from django.db import models
from django.utils import timezone

# Create your models here.

class PredictionHistorique(models.Model):
    # Les données d'entrer
    grossesse = models.IntegerField()
    glucose = models.IntegerField()
    pression_arterielle = models.IntegerField()
    epaisseur_peau = models.IntegerField()
    insuline = models.IntegerField()
    imc = models.FloatField()
    fonction_pedigree_diabete = models.FloatField()
    age = models.IntegerField()
    
    # Résultat
    resultat_prediction = models.CharField(max_length=50)
    probabilite = models.FloatField(null=True, blank=True)
    
    #metadonnées
    date_prediction = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    
    def __str__(self):
        return f"Préduction du {self.date_prediction.strftime('%d%m%Y')} - {self.resultat_prediction}"
    
    class Meta:
        ordering = ['-date_prediction']