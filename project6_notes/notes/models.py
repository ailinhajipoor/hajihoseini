from django.db import models


# Create your models here.
class Notes(models.Model):
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.author} : {self.text}"
