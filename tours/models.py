from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('safari', 'Safari'),
        ('weekend', 'Weekend Getaway'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='safari')
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField("image")
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Hotel(models.Model):
    BUDGET_CHOICES = [
        ('budget', 'Budget'),
        ('mid', 'Mid-range'),
        ('luxury', 'Luxury'),
    ]

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="hotels")
    name = models.CharField(max_length=200)
    budget_type = models.CharField(max_length=20, choices=BUDGET_CHOICES)

    description = models.TextField()
    features = models.TextField()  # meals, pool, tents, etc.

    def __str__(self):
        return f"{self.name} ({self.budget_type})"
