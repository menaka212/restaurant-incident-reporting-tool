from django.db import models
from django.contrib.auth.models import User
from stores.models import Store


class Incident(models.Model):

    CATEGORY_CHOICES = [
        ('POS Issue', 'POS Issue'),
        ('Delivery Delay', 'Delivery Delay'),
        ('Inventory', 'Inventory'),
        ('Kitchen Equipment', 'Kitchen Equipment'),
        ('Customer Complaint', 'Customer Complaint'),
        ('Other', 'Other'),
    ]

    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    severity = models.CharField(
        max_length=50,
        choices=SEVERITY_CHOICES
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Open'
    )

    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    attachment = models.ImageField(
        upload_to='incident_files/',
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title