from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    def __str__(self):
        return f"{self.name},{self.last_name},{self.phone_number}"
