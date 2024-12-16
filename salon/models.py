from django.db import models

# Create your models here.

from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Brand Name")
    country = models.CharField(max_length=100, verbose_name="Country of Origin")
    established_year = models.IntegerField(verbose_name="Year Established")

    def __str__(self):
        return self.name

class Cars(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model_name = models.CharField(max_length=100, verbose_name="Model Name")
    production_year = models.IntegerField(verbose_name="Production Year")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='cars/photos', blank=True, null=True)  # Rasm uchun maydon

    def __str__(self):
        return f"{self.model_name} ({self.brand.name})"
