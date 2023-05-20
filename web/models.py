from django.db import models

# Create your models here.
class Product(models.Model):
    LANG_CHOICES = (
        ('English', 'English'),
        ('Malayalam', 'Malayalam'),
        ('Arabic', 'Arabic'),
    )
    language = models.CharField(max_length=50, choices=LANG_CHOICES)
    author=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    price=models.FloatField()
    year=models.IntegerField()
    image=models.ImageField(upload_to="")
    publisher=models.CharField(max_length=50)
    pdf= models.FileField(upload_to="pdf")
    
    def __str__(self):
        return self.name
    
    
    