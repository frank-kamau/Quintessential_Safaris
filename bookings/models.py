from django.db import models
from tours.models import Tour
import uuid

# Create your models here.

class Booking(models.Model):
    reference = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        editable=False
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    persons = models.PositiveIntegerField()
    booked_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f"BT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tour', 'email'],
                name='unique_tour_booking_per_email'
            )
        ]

    def __str__(self):
        return f"{self.full_name} - {self.tour.title}"