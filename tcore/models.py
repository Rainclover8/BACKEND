from django.db import models

# Create your models here.
class model(models.Model):
    resim = models.FileField(verbose_name="resim", upload_to="media/resimler")
    baslik = models.CharField(max_length=20)
    aciklama = models.TextField(max_length=400)
    
    def __str__(self):
        return self.baslik
    
    
    
class accordion(models.Model):
    baslik = models.CharField(max_length=20)
    aciklama = models.TextField()
    
    def __str__(self):
        return self.baslik