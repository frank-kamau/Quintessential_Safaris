from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tour(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField("image")
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
