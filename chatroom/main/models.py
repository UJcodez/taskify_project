from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a default user (change as needed)
    title = models.CharField(max_length=100)
    date = models.DateField(default=date(2023, 1, 1))
    content = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    # Add other fields as needed for your user profile

    def __str__(self):
        return self.full_name
