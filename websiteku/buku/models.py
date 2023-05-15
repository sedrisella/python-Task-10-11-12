from django.db import models

# Create your models here.
class Kategori(models.Model):
    kategori = models.CharField(max_length=100)

    def __str__(self):
        return self.kategori

class Post(models.Model):
    judul = models.CharField(max_length=250)
    sinopsis = models.TextField()

    
class Post(models.Model):
    judul = models.CharField(max_length=250)
    sinopsis = models.TextField()
    kategori = models.ForeignKey(Kategori,on_delete=models.SET_NULL,null=True)

    def _str_(self):
        return self.judul